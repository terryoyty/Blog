from uuid import uuid4


def get_uuid():
    _uuid = ''.join(str(uuid4()).split('-'))
    return _uuid


if __name__ == '__main__':
    print(get_uuid())