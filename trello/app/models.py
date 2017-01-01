import binascii
import os

from django.db import models
from app.api.constants import *

class Users(models.Model):
    user_name = models.CharField(max_length=MAX_NAME_LENGTH)
    email = models.CharField(max_length=MAX_EMAIL_LENGTH, unique=True)
    password_hash = models.CharField(max_length=MAX_PASSWORD_LENGTH)
    user_id = models.AutoField(primary_key=True)
    board_ids = models.CharField(max_length=BOARD_ID_LENGTH)

    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        return super(Users, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user_name

class TokenManager(models.Manager):
    def generate_access_token(self):
        return binascii.hexlify(os.urandom(TOKEN_LENGTH/2)).decode()

    def get_access_token(self, user_id=None, access_token=None):
        if user_id:
            userid = Token.objects.get(user_id=user_id)
            return userid
        elif access_token:
            token = Token.objects.get(access_token=access_token)
            return token

        raise django_exc.ObjectDoesNotExist("access token object does not exists")


class Token(models.Model):
    access_token = models.CharField(max_length=TOKEN_LENGTH, primary_key=True)
    user = models.ForeignKey(Users)
    objects = TokenManager()

    def save(self, *args, **kwargs):
        if not self.access_token:
            self.access_token = Token.objects.generate_access_token()
        return super(Token, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.access_token


class Boards(models.Model):
    board_name = models.CharField(max_length=MAX_NAME_LENGTH)
    board_id = models.AutoField(primary_key=True)
    list_ids = models.CharField(max_length=LIST_ID_LENGTH)

    def save(self, *args, **kwargs):
        return super(Boards, self).save(*args, **kwargs)

class Lists(models.Model):
    list_name = models.CharField(max_length=MAX_NAME_LENGTH)
    list_id = models.AutoField(primary_key=True)
    card_ids = models.CharField(max_length=CARD_ID_LENGTH)

    def save(self, *args, **kwargs):
        return super(Lists, self).save(*args, **kwargs)

class Cards(models.Model):
    card_name = models.CharField(max_length=MAX_NAME_LENGTH)
    card_id = models.AutoField(primary_key=True)
    card_desc = models.CharField(max_length=CARD_DESC_LENGTH)
    card_due_date = models.DateField()
    card_status = models.BooleanField()

    def save(self, *args, **kwargs):
        return super(Cards, self).save(*args, **kwargs)

