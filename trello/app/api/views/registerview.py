from rest_framework import generics
from rest_framework  import mixins

from app.api.constants import *
from app.api.libraries import permissions
from app.api.libraries.customresponse import CustomResponse

from app.api.libraries.userlib import UserLib
from app.models import Users

"""
{
    "email": "a@b.com",
    "password": "abcd",
    "user_name": "name"
}
"""

user_lib = UserLib()

class RegisterView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    model = Users
    permission_classes = (permissions.IsAuthenticatedOrCreate, )

    def get(self, request):
        options = request.GET
        payload = user_lib.get_user(user=request.user)
        return CustomResponse(message="User details" , payload=payload, code=HTTP_200_OK)

    def post(self, request):
        try:
            user_details = request.data
            user_lib.add_user(user_details)
            return CustomResponse(message="User added", code=HTTP_201_CREATED)
        except Exception as e:
            return CustomResponse(message=str(e), code=HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        modifications = request.data
        user_lib.update_user(modifications=modifications, user=request.user)
        return CustomResponse(message="User updated", code=HTTP_200_OK)

    def delete(self, request):
        try:
            user_lib.delete_user(token=request.auth, user=request.user)
            return CustomResponse(message="User deleted", code=HTTP_200_OK)
        except Exception as e:
            return CustomResponse(message=str(e), code=HTTP_500_INTERNAL_SERVER_ERROR)
