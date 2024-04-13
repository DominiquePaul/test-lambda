import os
from inference_sdk import InferenceHTTPClient
# from roboflow import Roboflow


def handler(event, context):
    client = InferenceHTTPClient(api_url="https://detect.roboflow.com",
                                 api_key=os.environ["ROBOFLOW_API_KEY"])
    img_path = "./pizza.jpg"
    return client.infer(img_path, model_id="pizza-identifier/3")
