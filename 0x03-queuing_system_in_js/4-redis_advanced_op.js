#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const updateHash = (hashName, fieldName, fieldValue) => {
  client.HSET(hashName, fieldName, fieldValue, print);
};

const showHash = (hashName) => {
  client.HGETALL(hashName, (_err, reply) => console.log(reply));
};

function main() {
  const hashObject = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  for (const [field, value] of Object.entries(hashObject)) {
    updateHash('HolbertonSchools', field, value);
  }
  showtHash('HolbertonSchools');
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
