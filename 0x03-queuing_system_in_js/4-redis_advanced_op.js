import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

const hash = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
};

for (const [key, val] of Object.entries(hash)) {
  client.hset('HolbertonSchools', key, val, redis.print);
}

client.hgetall('HolbertonSchools', (err, reply) => {
  console.log(reply);
});
