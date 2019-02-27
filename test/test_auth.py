from src.auth import users, authorized

users['ghost'] = '6446d58d6dfafd58586d3ea85a53f4a6b3cc057f933a22bb58e188a74ac8f663'


def test_authorized():
    assert authorized('Basic Z2hvc3Q6Ym9v')


def test_not_authorized():
    assert not authorized('Basic Z2hvc3Q6Ym8=')


def test_not_found():
    assert not authorized('Basic Z2hvc3QyOmJvbw==')


def test_empty():
    assert not authorized(None)
    assert not authorized('')
