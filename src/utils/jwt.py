from config import DebugConfig
# from __main__ import app

import jwt
from functools import wraps
from flask import request, jsonify
from datetime import datetime, timedelta


def generate_jwt_token(user_id, user_email):
    token_generated = jwt.encode({
        'user': {
            'id': user_id,
            'email': user_email
        },
        'exp': datetime.utcnow() + timedelta(minutes=30)
    # }, app.config['SECRET_KEY'])
    }, DebugConfig.SECRET_KEY)

    return token_generated


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        uri_params = request.args
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            if uri_params.get('token'):
                token = uri_params.get('token')

        split = token.split()
        token = split[1] if len(split) == 2 else None

        if not token:
            return jsonify({
                'message': 'Token not found.',
            })

        try:
            data = jwt.decode(token, DebugConfig.SECRET_KEY, algorithms=['HS256'])
            # data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            # current_user = User.query.filter_by(public_id=data['public_id']).first()
            user = data

        except:
            return jsonify({'message': 'Invalid token.'})

        return f(user, *args, **kwargs)

    return decorator
