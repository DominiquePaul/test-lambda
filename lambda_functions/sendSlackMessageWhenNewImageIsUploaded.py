import json


def lambda_handler(event, context):
    print(json.dumps(event))  # For debugging: to see the event structure
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! v4')
    }
