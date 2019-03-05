import re
import base64
import json
import hashlib

users = {}


def load_users(path):
    with open(path) as f:
        users.update(json.load(f))


def authorized(token):
    if not token:
        print(f'Token is empty')
        return False

    m = re.match(r'^Basic (.*)', token)
    if not m:
        print(f'Token does not contain basic auth: {token}')
        return False

    user, password = base64.b64decode(m.group(1)).decode('utf8').split(':', 1)

    correct_hash = users.get(user)

    if correct_hash is None:
        print(f'User {user} not found in users.json')
        return False

    if correct_hash != hash_password(password):
        print(f'Incorrect password for {user}')
        return False

    return user


def hash_password(password):
    password_hash = hashlib.sha256()
    password_hash.update(password.encode())

    return password_hash.hexdigest()
