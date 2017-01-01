from rest_framework import generics
from rest_framework import mixins

from app.api.libraries.permissions import IsAuthenticatedOrCreate
from app.models import Users
from app.api.constants import *
from app.api.libraries.userlib import UserLib
from app.api.libraries.tokenlib import TokenLib

from app.api.libraries.customresponse import CustomResponse

user_lib = UserLib()
token_lib = TokenLib()

"""
{
    "email": "a@b.com",
    "password": "abcd"
}
"""

class LoginView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    model = Users
    permission_classes = (IsAuthenticatedOrCreate, )

    def post(self, request):
        try:
            global user_lib, token_lib
            signin_details = request.data
            access_token, created = user_lib.authenticate_user(signin_details=signin_details)
            message="Logged in"
            if created:
                message = "Logged in"
            return CustomResponse(message=message, payload={"Token": access_token}, code=HTTP_200_OK)
        except Exception as e:
            return CustomResponse(message=str(e), code=HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        token_lib.delete_access_token(token=request.auth)
        return CustomResponse(message="Logged out", code=HTTP_200_OK)
