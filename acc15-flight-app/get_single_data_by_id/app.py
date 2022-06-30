import json
import os
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_name = os.getenv('TABLE_NAME')
    table = dynamodb.Table(table_name)
    
    response = table.get_item(Key={"id": event['id']})
    return {
        'statusCode': 200,
        'body': response
    }
