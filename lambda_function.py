import os
import json
# from inference_sdk import InferenceHTTPClient
from roboflow import Roboflow


def handler(event, context):
    rf = Roboflow(api_key=os.environ["ROBOFLOW_API_KEY"])
    project = rf.workspace().project("pizza-identifier")
    model = project.version(3).model

    # infer on a local image
    return model.predict("pizza.jpg", confidence=40, overlap=30).json()
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
