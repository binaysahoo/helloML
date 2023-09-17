const express = require('express');
const MongoClient = require('mongodb').MongoClient;

const app = express();
const port = 3000;

// MongoDB connection URL
const mongoUrl = 'mongodb://localhost:27017/regrundb';

app.get('/tests', async (req, res) => {
  try {
    // Connect to MongoDB
    const client = await MongoClient.connect(mongoUrl, { useNewUrlParser: true });
    const db = client.db();

    // Your MongoDB aggregation query goes here
    const aggregationPipeline = [
      {
        $match: {
        //status: 'pass',
        sdate: { $lte: new Date('2023-09-05T00:00:00Z') },
        edate: { $gte: new Date('2023-09-01T00:00:00Z') }
        }
      },
      {
        $group: {
        _id: '$test',
        totalFailures: { $sum: { $cond: [{ $eq: ['$status', 'fail'] }, 1, 0] } }
        }
      },
      {
        $match: { totalFailures: 0 }
      },
      {
        $project: { _id: 0, test: '$_id' }
      }
    ];

    const results = await db.collection('regdata').aggregate(aggregationPipeline).toArray();

    // Close the MongoDB connection
    client.close();

    // Send the results as JSON to the client
    res.json(results);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'An error occurred' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
