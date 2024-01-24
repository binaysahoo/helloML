import pika
import json
from faker import Faker
# Connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='empqueue')

fake = Faker() 
# Data to be published (as a JSON message)
#message_data = {'key': 'value'}
message_data = {
    "name": fake.name(),
    "email" : fake.email(),
    "city" : fake.city()
 }

# Convert Python dictionary to a JSON string
message_body = json.dumps(message_data)

# Publish the message to the queue
channel.basic_publish(exchange='', routing_key='empqueue', body=message_body)

print(f" [x] Sent: {message_body}")

# Close the connection
connection.close()
