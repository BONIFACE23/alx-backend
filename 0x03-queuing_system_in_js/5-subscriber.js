import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

const channelName = 'holberton school channel';

client.subscribe(channelName, (err, count) => {
  if (err) {
    console.error('Error subscribing to channel:', err);
    return;
  }
    console.log(`Subscribed to channel: ${channelName} (count: ${count})`);
});

client.on('message', (channel, message) => {
    if (channel === channelName) {
      console.log(message);
      if (message === 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
      }
    }
});
