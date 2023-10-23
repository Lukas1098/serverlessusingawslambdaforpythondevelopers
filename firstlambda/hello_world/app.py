import json


def first_lambda(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Aws Lambda is super cool",

        }),
    }
