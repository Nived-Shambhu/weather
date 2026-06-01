import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('weather_table')

def lambda_handler(event, context):
    pass

import requests

API_KEY = "YOUR_API_KEY"

city = "Kochi"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

data['main']['temp']
data['main']['humidity']
data['weather'][0]['description']

from datetime import datetime

datetime.utcnow().isoformat()

item = {
    'city': city,
    'temperature': str(data['main']['temp']),
    'humidity': str(data['main']['humidity']),
    'weather': data['weather'][0]['description'],
    'timestamp': datetime.utcnow().isoformat()
}

table.put_item(Item=item)