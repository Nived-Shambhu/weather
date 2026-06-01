import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('weather_table')

def lambda_handler(event, context):
    pass