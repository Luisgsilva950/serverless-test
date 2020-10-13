import json


def hello(event, context):
    body = {
        "message": "Nice! I can do a Serverless system!",
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
