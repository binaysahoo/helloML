import requests
from faker import Faker
import json
import random
import time

fake = Faker()

def generate_fake_message():
    return {
        'name': fake.name(),
        'email': fake.email(),
        'city': fake.city(),
        'age': random.randint(18, 99),
    }

def post_message(url, message):
    headers = {'Content-Type': 'application/json'}
    print(json.dumps(message))
    response = requests.get(url, data=json.dumps(message), headers=headers)

    if response.status_code == 200:
        print(f"Message posted successfully: {message}")
    else:
        print(f"Failed to post message. Status Code: {response.status_code}, Response: {response.text}")

if __name__ == '__main__':
    flask_url = 'http://localhost:5000/consume'

    while True:
        fake_message = generate_fake_message()
        post_message(flask_url, fake_message)

        # Sleep for a random interval (e.g., between 1 to 5 seconds)
        time.sleep(random.uniform(1, 5))
