from django.core.validators import validate_email
from django.core import exceptions

from app.api.constants import *

def validate_user_email(email_id):
    try:
        validate_email(email_id)
        if len(email_id) <= MAX_EMAIL_LENGTH:
            return True
    except:
        pass

    raise exceptions.ValidationError("Enter a valid email address within %d chars"% MAX_EMAIL_LENGTH, code=HTTP_400_BAD_REQUEST)


def validate_user_name(name):
    if len(name) <= MAX_NAME_LENGTH and len(name) >= MIN_NAME_LENGTH and name.isalnum():
        return True

    raise exceptions.ValidationError("Enter a valid alphanumeric username within length", code=HTTP_400_BAD_REQUEST)


def validate_user_password(password):
    if len(password) >= MIN_PASSWORD_LENGTH and len(password) <= MAX_PASSWORD_LENGTH:
        return True

    raise exceptions.ValidationError("invalid password length", code=HTTP_400_BAD_REQUEST)


def validate_user_details(user_details):
    if not user_details:
        raise exceptions.ValidationError("Empty signup request", code=HTTP_400_BAD_REQUEST)

    return \
        validate_user_email(user_details[EMAIL_ID]) and \
        validate_user_password(user_details[PASSWORD]) and \
        validate_user_name(user_details[USER_NAME])


def validate_modifications(modifications):
    if not modifications:
        raise exceptions.ValidationError("Empty update request", code=HTTP_400_BAD_REQUEST)
    if USER_NAME in modifications:
        validate_user_name(modifications[USER_NAME])
    if PASSWORD in modifications:
        validate_user_password(modifications[PASSWORD])

    return True


def validate_signin_details(signin_details):
    if not signin_details:
        raise exceptions.ValidationError("Empty signin request", code=HTTP_400_BAD_REQUEST)
    return \
        validate_user_email(signin_details[EMAIL_ID]) and \
        validate_user_password(signin_details[PASSWORD])


def validate_not_empty(data):
    if not data:
        raise exceptions.ValidationError("Empty request", code=HTTP_400_BAD_REQUEST)

