import redis from "redis";

const client = redis.createClient();

client
  .on("error", (error) => {
    if (error) console.log(`Redis client not connected to the server: ${err}`);
  })
  .on("ready", () => {
    console.log("Redis client connected to the server");
  });

const Message = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish("holberton school channel", message);
  }, time);
};
Message("Holberton Student #1 starts course", 100);
Message("Holberton Student #2 starts course", 200);
Message("KILL_SERVER", 300);
Message("Holberton Student #3 starts course", 400);
