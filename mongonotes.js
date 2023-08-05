const { MongoClient } = require('mongodb');

// Connection URL
const url = 'mongodb://localhost:27017';

// Database name
const dbName = 'your_database_name';

async function main() {
  const client = new MongoClient(url);

  try {
    // Connect to MongoDB
    await client.connect();

    // Get a reference to the database
    const db = client.db(dbName);

    // Sample common elements
    const commonElements = [
      { name: 'John', age: 30 },
      { name: 'Alice', age: 25 },
      // Add more common elements as needed
    ];

    // Step 1: Insert common elements into the 'maininfo' collection and get their '_id'
    const mainInfoCollection = db.collection('maininfo');
    const mainInfoIds = await mainInfoCollection.insertMany(commonElements).then(result => result.insertedIds);

    // Step 2: Use '_id' as a reference in the 'otherinfo' collection
    const otherInfoCollection = db.collection('otherinfo');

    // Example documents in the 'otherinfo' collection referencing the common elements
    const otherInfoDocuments = [
      { maininfo_id: mainInfoIds[0], otherData: 'Some data for John' },
      { maininfo_id: mainInfoIds[1], otherData: 'Some data for Alice' },
      // Add more documents referencing the common elements as needed
    ];

    await otherInfoCollection.insertMany(otherInfoDocuments);

    console.log('Data insertion successful.');
  } catch (err) {
    console.error('Error:', err);
  } finally {
    // Close the connection
    client.close();
  }
}

main().catch(console.error);
