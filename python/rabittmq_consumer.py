import pika
import json
from pymongo import MongoClient

# Connection parameters for MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['rabittmqdb']  # Replace 'my_database' with your desired database name
collection = db['empdata']  # Replace 'my_collection' with your desired collection name

def callback(ch, method, properties, body):
    # Decode the JSON message
    message = json.loads(body.decode('utf-8'))
    print(f" [x] Received : {message}")

    # Insert the JSON data into MongoDB
    insert_result = collection.insert_one(message)
    
    
    print(f" MongoDB Insert ID: {insert_result.inserted_id}")

# Connection parameters for RabbitMQ
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the same queue
channel.queue_declare(queue='empqueue')

# Set up the callback function to handle incoming messages
channel.basic_consume(queue='empqueue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
