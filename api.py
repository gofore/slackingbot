import json
import os
import logging
import urllib

print('Loading function')
# BOT_TOKEN = os.environ["BOT_TOKEN"]


def send_slack_message(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


def get_historical_messages(event, context):

    if "challenge" in event['body']:
        print("Hellurei")
        return event["challenge"]

    logging.warn(json.dumps(event))
    body = {
        "hello": "world"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def slack_event_handler(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
