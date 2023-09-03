const redis = require('redis');
const { MongoClient } = require('mongodb');
const express = require('express');



// Create a Redis client
const redisClient = redis.createClient({
  host: 'localhost', // Redis server hostname
  port: 6379,        // Redis server port
});

const mongoURI = 'mongodb://localhost:27017';

// Create a MongoDB client
const mongoClient = new MongoClient(mongoURI);

// Connect to MongoDB 
(async () => {
  try {
    await mongoClient.connect();
    console.log('Connected to MongoDB');    
  } catch (err) {
    console.error('Error connecting to MongoDB:', err);
  }
})();
// Connect to Redsis
(async () => {
    await redisClient.connect();
})();

redisClient.on('ready', () => {
    console.log("Redis Connected!");
});  
redisClient.on('error', (err) => {
    console.error(err);
});


/**********************************************************
    RESTAPI
***********************************************************/
const app = express();
const port = 3000;
const host = "localhost";
// Route to handle GET requests
app.get('/', (req, res) => {
    res.send('Welcome to Upskill');
});

  
// Route to handle dynamic URL parameters
http://localhost:3000/users/binayk
app.get('/users/:userId', (req, res) => {
    const userId = req.params.userId;
    res.send(`User ID: ${userId}`);
});
  
// Route for handling query parameters
// http://localhost:3000/query?name=binay&age=20
app.get('/query', (req, res) => {
    const name = req.query.name;
    const age = req.query.age;
    res.json({ name, age });
});

// Start the Express server
app.listen(port, () => {
    console.log(`Server is running on port http://${host}:${port}/`);
});
/**********************************************************

***********************************************************/

// Define a route to get data
//http://localhost:3000/empdetails/binayk
app.get('/empdetails/:userid', async (req, res) => {
  
  const userid = req.params.userid;
  const key = 'userid:'+userid;
  // Data not found in Redis, fetch it from MongoDB
  const db = mongoClient.db('upskill');
  const collection = db.collection('redismongo');
  console.log(`userId: ${userid}`);
  try {
        (async () => {    
            const redisData = await redisClient.get(key);
            if (redisData) {
                // Data found in Redis
                console.log('Data retrieved from Redis');
                res.send(redisData);
            } else {
                const mongoData = await collection.findOne({ "userid":userid });
                // Data found in MongoDB, store it in Redis for future requests
                if (mongoData) {      
                    (async () => {    
                        await redisClient.set(key, JSON.stringify(mongoData), 'EX', 3600); // Set an expiry of 1 hour (3600 seconds)
                    })();
                    console.log('Data retrieved from MongoDB and stored in Redis');
                    res.json(mongoData);
                    } else {
                    console.log('Data not found in MongoDB');
                    res.status(404).send('Data not found');
                    }        
                }            
        })();
        
    } catch (mongoErr) {
        console.error('MongoDB Error:', mongoErr);
        res.status(500).send('Internal Server Error');
    }

 
});
