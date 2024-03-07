// const async = require("async")
// const kafka = require("kafka-node")
const { Kafka, logLevel  } = require('kafkajs')

// https://www.npmjs.com/package/kafkajs#getting-started
// https://kafka.js.org/docs/getting-started

const kafka = new Kafka({
  clientId: 'my-app',
  brokers: ['host1:9094','host2:9094','host3:9094'],
  requestTimeout: 25000,
  retry: {
    initialRetryTime: 100,
    retries: 10
  },
  logLevel: logLevel.ERROR
})
kafka.logger().setLogLevel(logLevel.WARN)

// producer
const producer = kafka.producer({
  allowAutoTopicCreation: false,
  transactionTimeout: 30000
})
producer.logger().setLogLevel(logLevel.INFO)

const msgs = [ 
  { key: 'empdetails', value: '{"name":"binay kumar","age":19}' ,partition: 0},
  { key: 'metainfo', value: 'Learning kafka', partition: 1, timestamp: Date.now(),
    headers: {
      'id': '2bfb68bb',
      'systemid': 'my-system'
    }
  }
]

const topicMessages = [
  {
    topic: 'topic-a',
    messages: [{ key: 'key', value: 'hello topic-a' }],
  },
  {
    topic: 'topic-b',
    messages: [{ key: 'key', value: 'hello topic-b' }],
  },
  {
    topic: 'topic-c',
    messages: [
      {
        key: 'key',
        value: 'hello topic-c',
        headers: {
          'correlation-id': '2bfb68bb-893a-423b-a7fa-7b568cad5b67',
        },
      }
    ],
  }
]

const run = async () => {
  // Producing
  await producer.connect()
  console.log("producing message:",msgs)

  // send single topic
  await producer.send({
    topic: 'test-topic',
    messages: msgs,
    //acks: 1,
    timeout: 30000 // ms    
  })

  // send batch
  await producer.sendBatch({ topicMessages })
}

run().catch(console.error)
