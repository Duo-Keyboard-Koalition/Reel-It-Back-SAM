import json
import boto3
import os
import pandas as pd
from io import BytesIO
import base64

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    try:
        # Decode the base64 encoded file content
        file_content = base64.b64decode(event['body'])

        # Read the Excel file
        df = pd.read_excel(BytesIO(file_content))

        # Iterate over the rows and put them into DynamoDB
        for index, row in df.iterrows():
            item = row.to_dict()
            table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Excel file uploaded successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }