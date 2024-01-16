from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import pika
import json
import threading

app = Flask(__name__)

# Configure MongoDB connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)

# Configure RabbitMQ connection
rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
rabbitmq_channel = rabbitmq_connection.channel()
rabbitmq_channel.queue_declare(queue='data_queue')

# Define the MongoDB collection
collection = mongo.db.mycollection

def process_data_queue():
    """
    Background thread function to consume messages from the RabbitMQ data_queue
    and insert data into MongoDB.
    """
    def callback(ch, method, properties, body):
        try:
            # Process the message and insert data into MongoDB
            data_to_insert = json.loads(body.decode('utf-8'))
            collection.insert_one(data_to_insert)
            print(f"Data inserted into MongoDB: {data_to_insert}")

        except Exception as e:
            print(f"Error processing message: {str(e)}")

    rabbitmq_channel.basic_consume(queue='data_queue', on_message_callback=callback, auto_ack=True)
    rabbitmq_channel.start_consuming()

# Start the background thread to process the data queue
data_queue_thread = threading.Thread(target=process_data_queue)
data_queue_thread.daemon = True
data_queue_thread.start()

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

            # Publish the data to the RabbitMQ data_queue
            rabbitmq_channel.basic_publish(exchange='', routing_key='data_queue', body=json.dumps(data_to_insert))
            print(f"Data queued for insertion: {data_to_insert}")

            return jsonify({'status': 'success', 'message': 'Data queued for insertion'}), 202

        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
