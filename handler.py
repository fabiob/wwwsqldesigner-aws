import os
import json
import boto3

from actions import save, load, list_keywords
from utils import respond


def backend(event, context):
    """
    Handles wwwsqldesigner backend operations
    """

    method = event['httpMethod']
    qs = event['queryStringParameters']
    body = event['body']

    action = qs.get('action')
    keyword = qs.get('keyword')

    if method == 'POST' and action == 'save':
        return save(keyword, body)
    if method == 'GET' and action == 'load':
        return load(keyword)
    if method == 'GET' and action == 'list':
        return list_keywords()

    return respond(f'Unrecognized action: {method} {action}', code=400)
