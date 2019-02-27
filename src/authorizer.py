from .auth import load_users, authorized

load_users('users.json')


def authorize(event, context):
    auth_user = authorized(event['authorizationToken'])

    if not auth_user:
        raise Exception('Unauthorized')

    return make_policy(auth_user, event['methodArn'])


def make_policy(user, resource):
    return {
        'principalId': user,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': 'Allow',
                    'Resource': resource
                }
            ]
        }
    }
