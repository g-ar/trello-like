from app.api.constants import *
from app.models import Users, Boards, Token
from app.api.helpers import validators

from rest_framework import exceptions as rest_exc
from django.core import exceptions as django_exc

import hashlib
import json


class UserLib():
    def password_hash(self, password):
        hash_library = hashlib.new(HASH_METHOD)
        hash_library.update(password)
        _hash = hash_library.hexdigest()
        return _hash

    def is_unique_email(self, email):
        if not Users.objects.filter(email=email).exists():
           return True
        raise django_exc.ValidationError('Email address already exists', code=HTTP_400_BAD_REQUEST)

    def add_user(self, user_details):
        if validators.validate_user_details(user_details) and  self.is_unique_email(user_details[EMAIL_ID]):
            server_hash = self.password_hash(user_details[PASSWORD])
            user_details[PASSWORD_HASH] = server_hash
            del user_details[PASSWORD]
            user_details[BOARD_IDS] = "[]"
            Users.objects.create(**user_details)

    def get_board_id_list(self, user):
        tmp = Users.objects.filter(user_name=user).values()[0]
        if tmp.get(BOARD_IDS):
            return json.loads(tmp[BOARD_IDS])
        return []
    
    def update_board_id_list(self, user, board_id):
        b_list = self.get_board_id_list(user)
        b_list.append(board_id)
        vals = ({BOARD_IDS: json.dumps(b_list)})
        Users.objects.filter(user_name=user).update(**vals)
        
    def get_user(self, user):
        tmp = Users.objects.filter(user_name=user).values()
        if tmp:
            tmp = tmp[0]
            del tmp[USER_ID]
            del tmp[PASSWORD_HASH]
            board_ids = json.loads(tmp[BOARD_IDS])            
            del tmp[BOARD_IDS]
            bobj = Boards.objects.filter(board_id__in=board_ids).values()
            boards = []
            for b_id in board_ids:
                boards += [{BOARD_ID: b[BOARD_ID], BOARD_NAME: b[BOARD_NAME]} for b in bobj if b[BOARD_ID] == b_id]
            tmp[BOARDS] = boards
            
        return tmp
    
    def update_user(self, modifications, user):
        if validators.validate_modifications(modifications=modifications):
            if USER_NAME in modifications:
                user.user_name = modifications[USER_NAME]

            if PASSWORD_HASH in modifications:
                _hash = self.password_hash(modifications[PASSWORD_HASH])
                user.password_hash = _hash

            if BOARD_IDS in modifications:
                user.board_ids = modifications[BOARD_IDS]
            user.save()

    def delete_user(self, token, user):
        token.delete()
        Users.objects.filter(user_name=user).delete()

    def authenticate_user(self, signin_details):
        email = signin_details[EMAIL_ID]
        password = signin_details[PASSWORD]
        validators.validate_signin_details(signin_details=signin_details)
        user = Users.objects.get(email=email)
        client_hash = self.password_hash(password=password)
        hash_stored_in_db = user.password_hash
    
        if hash_stored_in_db == client_hash:
            token, created = Token.objects.get_or_create(user=user)
            return token.access_token, created
        raise rest_exc.AuthenticationFailed('Invalid email or password')

