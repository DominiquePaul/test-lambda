import os
from inference_sdk import InferenceHTTPClient
# from roboflow import Roboflow


def handler(event, context):
    # initialize the client
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key=os.environ["ROBOFLOW_API_KEY"]
    )

    # infer on a local image
    img_path = "./pizza.jpg"
    result = CLIENT.infer(img_path, model_id="pizza-identifier/3")
    return result
