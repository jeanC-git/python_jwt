from flask import Blueprint
from src.utils.jwt import token_required, generate_jwt_token
from src.models.User import User

auth = Blueprint("auth", __name__)
base_uri = "auth"


@auth.route('/generate-jwt', methods=['GET'])
def generate_jwt():
    user = User.query.filter_by(id=1).first()
    token = generate_jwt_token(user_id=user.id, user_email=user.email)

    return {
        'token': token
    }


@auth.route('/me', methods=['GET'])
@token_required
def me(user):
    return {
        'user': user,
    }
