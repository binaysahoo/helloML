// const async = require("async")
// const kafka = require("kafka-node")
const { Kafka } = require('kafkajs')

// https://www.npmjs.com/package/kafkajs#getting-started
// https://kafka.js.org/docs/getting-started

const kafka = new Kafka({
  clientId: 'my-app',
  brokers: ['host1:9094','host2:9094','host3:9094']
})

const consumer = kafka.consumer({ groupId: 'test-group' })

const run = async () => {
 
  // Consuming
  await consumer.connect()
  await consumer.subscribe({ topic: 'test-topic', fromBeginning: true })

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      console.log({
        topic,
        partition,
        offset: message.offset,
        key: message.key.toString(),
        timestamp:message.timestamp,        
        value: message.value.toString()
        //headers: message.headers.toString()
      })
    },
  })
}

run().catch(console.error)
