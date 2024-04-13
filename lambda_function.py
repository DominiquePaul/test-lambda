import os
import json
from inference_sdk import InferenceHTTPClient


def handler(event, context):
    client = InferenceHTTPClient(api_url="https://detect.roboflow.com",
                                 api_key=os.environ["ROBOFLOW_API_KEY"])
    img_path = "./pizza.jpg"
    return client.infer(img_path, model_id="pizza-identifier/3")
    print("Wink emoji")

    print(json.dumps(event))  # For debugging: to see the event structure
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! v4')
    }
