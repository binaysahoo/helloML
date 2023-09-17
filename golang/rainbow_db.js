/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds

// Select the database to use.
use('upskill');
/*

// Insert a few documents into the sales collection.
db.getCollection('regdata').insertMany([
  { 'test': 't1', 'diff': 'd1', 'status': 'pass', 'sdate': new Date('2023-09-01T00:00:00Z') ,'edate':  new Date('2023-09-05T00:00:00Z') },
  { 'test': 't2', 'diff': 'd1', 'status': 'pass', 'sdate': new Date('2023-09-01T00:00:00Z') ,'edate':  new Date('2023-09-05T00:00:00Z') },
  { 'test': 't3', 'diff': 'd1', 'status': 'fail', 'sdate': new Date('2023-09-02T00:00:00Z') ,'edate':  new Date('2023-09-03T23:59:59Z') },
  { 'test': 't3', 'diff': 'd1', 'status': 'pass', 'sdate': new Date('2023-09-01T00:00:00Z') ,'edate':  new Date('2023-09-01T23:59:59Z') },
  { 'test': 't3', 'diff': 'd1', 'status': 'pass', 'sdate': new Date('2023-09-04T00:00:00Z') ,'edate':  new Date('2023-09-05T23:59:59Z') },
  { 'test': 't4', 'diff': 'd1', 'status': 'pass', 'sdate': new Date('2023-09-01T00:00:00Z') ,'edate':  new Date('2023-09-05T00:00:00Z') },
  { 'test': 't5', 'diff': 'd1', 'status': 'pass', 'sdate': new Date('2023-09-01T00:00:00Z') ,'edate':  new Date('2023-09-05T00:00:00Z') },
  { 'test': 't6', 'diff': 'd1', 'status': 'pass', 'sdate': new Date('2023-09-01T00:00:00Z') ,'edate':  new Date('2023-09-05T00:00:00Z') },
  { 'test': 't7', 'diff': 'd1', 'status': 'pass', 'sdate': new Date('2023-09-01T00:00:00Z') ,'edate':  new Date('2023-09-05T00:00:00Z') },


]);

// Run a find command to view items sold on April 4th, 2014.
const salesOnApril4th = db.getCollection('sales').find({
  date: { $gte: new Date('2014-04-04'), $lt: new Date('2014-04-05') }
}).count();

// Print a message to the output window.
console.log(`${salesOnApril4th} sales occurred in 2014.`);

// Here we run an aggregation and open a cursor to the results.
// Use '.toArray()' to exhaust the cursor to return the whole result set.
// You can use '.hasNext()/.next()' to iterate through the cursor page by page.
db.getCollection('sales').aggregate([
  // Find all of the sales that occurred in 2014.
  { $match: { date: { $gte: new Date('2014-01-01'), $lt: new Date('2015-01-01') } } },
  // Group the total sales for each product.
  { $group: { _id: '$item', totalSaleAmount: { $sum: { $multiply: [ '$price', '$quantity' ] } } } }
]);
*/
// SCENARIO ONE

db.getCollection('regdata').aggregate([
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
]);


db.regdata.aggregate([
  {   
    $match: {
      $and: [
        {
          $and: [
            { sdate: { $lte: ISODate('2023-09-01T00:00:00Z') } },
            { edate: { $gte: ISODate('2023-09-01T00:00:00Z') } },
          ],
        },
        {
          $and: [
            { sdate: { $lte: ISODate('2023-09-03T23:59:59Z') } },
            { edate: { $gte: ISODate('2023-09-03T23:59:59Z') } },
          ],
        },
      ],
    },    
  },
  {
    $group:{
      _id: "$test",   
      failCount: { $sum: { $cond: [ {$eq: ["$status", "fail"]}, 1, 0,], }, },
      passCount: { $sum: { $cond: [ {$eq: ["$status", "pass"]}, 1, 0,], }, },
    }
  },
  {
    $match: { failCount: 0 }
  },
  {
    $project: {  _id: 0,test: '$_id' }
  },
  {
    $group: {  _id: null, tests: { $push: '$test' } }
  },
  {
    $project: { _id: 0, tests: 1 }
  }
])
