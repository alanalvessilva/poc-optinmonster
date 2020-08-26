import datetime
import os
import jwt


def create_jwt_token(data):
    data['exp'] = datetime.datetime.utcnow() + \
                  datetime.timedelta(minutes=int(os.environ.get('JWT_HOOK_TIME_EXP')))
    return jwt.encode(data, os.environ.get('JWT_HOOK_SECRET_KEY'), algorithm='HS256').decode()
