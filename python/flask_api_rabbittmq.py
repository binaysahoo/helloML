from flask import Flask, request, jsonify
from pymongo import MongoClient
import pika
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB connection
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['rabittmqdb']
collection = db['empdata']

# RabbitMQ connection
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.queue_declare(queue='empqueue')

def callback(ch, method, properties, body):
    # Decode the JSON message
    message = json.loads(body.decode('utf-8'))

    # Insert the JSON data into MongoDB
    insert_result = collection.insert_one(message)
    
    print(f" [x] Received and inserted into MongoDB: {message}")
    print(f" MongoDB Insert ID: {insert_result.inserted_id}")

# Set up the RabbitMQ consumer
channel.basic_consume(queue='empqueue', on_message_callback=callback, auto_ack=True)

@app.route('/consume', methods=['POST'])
def consume():
    try:
        # Receive JSON message from the request
        message = request.get_json()

        # Publish the message to RabbitMQ
        channel.basic_publish(exchange='', routing_key='empqueue', body=json.dumps(message))

        return jsonify({"status": "Message sent and consumed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/consumedata', methods=['GET'])
def consume():
    try:
        # Receive JSON message from the request
        message = request.get_json()

        # Publish the message to RabbitMQ
        channel.basic_publish(exchange='', routing_key='empqueue', body=json.dumps(message))

        return jsonify({"status": "Message sent and consumed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True)
