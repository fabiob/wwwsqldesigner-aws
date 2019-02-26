from .env import S3_PREFIX


def respond(body=None, mime="text/plain", code=200):
    return {"statusCode": code, "body": body, "headers": {"Content-Type": mime}}


def fn(keyword):
    return f'{S3_PREFIX}{keyword}.xml'


def fix(filename):
    return filename[len(S3_PREFIX):-4]
