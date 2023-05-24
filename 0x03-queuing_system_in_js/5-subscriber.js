import { createClient } from 'redis';

const client = createClient();
const exit = 'KILL_SERVER';


client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel');

client.on('message', (err, msg) => {
  console.log(msg);
  if (msg === exit) {
    client.unsubscribe();
    client.quit();
  }
});
client.on('error', err => {
  console.log('Redis client not connected to the server:', err.toString());
});
