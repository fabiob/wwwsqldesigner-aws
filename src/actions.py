import os
import json
import boto3

from .env import S3_BUCKET, S3_PREFIX
from .utils import respond, fix, fn

s3 = boto3.client('s3')


def save(keyword, body):
    s3.put_object(Bucket=S3_BUCKET, Key=fn(keyword), Body=body)

    return respond(code=201)


def load(keyword):
    response = s3.get_object(Bucket=S3_BUCKET, Key=fn(keyword))

    return respond(response['Body'].read().decode('utf-8'), mime='application/xml')


def list_keywords():
    response = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=S3_PREFIX)

    keywords = [fix(entry['Key'])
                for entry in response.get('Contents', list())]

    return respond("\n".join(keywords))
