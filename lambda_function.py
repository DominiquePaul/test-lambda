import json
import boto3
import numpy
import cv2


def handler(event, context):
    print("Loooool hello")
    print(dir(boto3))
    print(dir(numpy))
    print(dir(cv2))

    print(json.dumps(event))  # For debugging: to see the event structure
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! v4')
    }
