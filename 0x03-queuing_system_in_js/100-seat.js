import redis from "redis";
import kue from "kue";
import express from "express";
import { promisify } from 'util';

const client = redis.createClient();

let reservationEnabled = true;

const reserveSeat = (number) => {
  return promisify(client.set).bind(client)('available_seats', number);
};

const getAvailableSeats = async () => {
  const getVal = promisify(client.get).bind(client);
  return (await getVal('available_seats'));
};

const queue = kue.createQueue();

const app = express();

app.get('/available_seats', async (_req, res) => {
  const sets = await getAvailableSeats();
  res.json({numberOfAvailableSeats: sets});
});

app.get('/reserve_seat', (_req, res) => {
  if (!reservationEnabled) {
    res.json({ status: "Reservation are blocked" });
    return;
  }
  try {
    const job = queue.create('reserve_seat');

    job.on('failed', (error) => {
      console.log(`Seat reservation job ${job.id} failed: ${error}`);
    });

    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    });
    job.save();
    res.json({ status: 'Reservation in process' });
  } catch (e) {
    res.json({ status: 'Reservation failed' });
  }
});

app.get('/process', async (_req, res) => {
    res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async (_job, done) => {
    getAvailableSeats()
      .then((result) => Number.parseInt(result || 0))
      .then((sets) => {
        reservationEnabled = sets <= 1 ? false : reservationEnabled;
        if (sets >= 1) {
          reserveSeat(sets - 1)
            .then(() => done());
        } else {
          done(new Error('Not enough seats available'));
        }
    });
  });
});

app.listen(1245, () => {
  reserveSeat(50);
  console.log('Server running on localhost:1245');
});

export default app;
