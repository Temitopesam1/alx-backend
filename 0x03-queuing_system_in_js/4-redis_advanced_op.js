import { createClient, print } from 'redis';

const client = createClient();


const createHash = (key, field, value) => {
  client.hset(key, field, value, print);
};

const displayHash = (key) => {
  client.hgetall(key, (err, result) => console.log(result));
};

function main() {
  const hashObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  const key = 'HolbertonSchools';
  for (const [field, value] of Object.entries(hashObj)) {
    createHash(key, field, value);
  }
  displayHash(key);
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});

client.on('error', err => {
  console.log('Redis client not connected to the server:', err.toString());
});
