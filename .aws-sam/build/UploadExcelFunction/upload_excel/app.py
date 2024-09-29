import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    try:
        # Parse the JSON file content
        data = json.loads(event['body'])

        # Iterate over the items and put them into DynamoDB
        for item in data:
            table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'JSON file uploaded successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }