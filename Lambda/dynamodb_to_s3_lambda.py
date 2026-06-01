import json
import boto3

s3 = boto3.client('s3')

BUCKET_NAME = 'weather-project-bucket-123'

def lambda_handler(event, context):
    pass

for record in event['Records']:
    if record['eventName'] in ['INSERT', 'MODIFY']:
        pass

new_image = record['dynamodb']['NewImage']

data = {}

for key, value in new_image.items():
    data[key] = list(value.values())[0]