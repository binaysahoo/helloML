from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from confluent_kafka import Producer, Consumer, KafkaError
import json
import threading

app = Flask(__name__)

# Configure MongoDB connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)

# Configure Kafka producer
kafka_bootstrap_servers = 'localhost:9092'
kafka_topic = 'data_topic'
kafka_producer_config = {'bootstrap.servers': kafka_bootstrap_servers}
kafka_producer = Producer(kafka_producer_config)

# Configure Kafka consumer
kafka_consumer_config = {'bootstrap.servers': kafka_bootstrap_servers, 'group.id': 'my_group'}
kafka_consumer = Consumer(kafka_consumer_config)
kafka_consumer.subscribe([kafka_topic])

# Define the MongoDB collection
collection = mongo.db.mycollection

def process_kafka_messages():
    """
    Background thread function to consume messages from the Kafka data_topic
    and insert data into MongoDB.
    """
    while True:
        msg = kafka_consumer.poll(timeout=1000)  # 1 second timeout

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        try:
            # Process the received message and insert data into MongoDB
            data_to_insert = json.loads(msg.value().decode('utf-8'))
            collection.insert_one(data_to_insert)
            print(f"Data inserted into MongoDB: {data_to_insert}")

        except Exception as e:
            print(f"Error processing Kafka message: {str(e)}")

# Start the background thread to process Kafka messages
kafka_thread = threading.Thread(target=process_kafka_messages)
kafka_thread.daemon = True
kafka_thread.start()

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        # Retrieve all data from MongoDB
        data = collection.find()
        return dumps(data), 200

    elif request.method == 'POST':
        try:
            # Get JSON data from the request
            data_to_insert = request.json

            # Produce the data to the Kafka data_topic
            kafka_producer.produce(kafka_topic, key=None, value=json.dumps(data_to_insert))
            kafka_producer.flush()

            print(f"Data queued for insertion: {data_to_insert}")

            return jsonify({'status': 'success', 'message': 'Data queued for insertion'}), 202

        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
