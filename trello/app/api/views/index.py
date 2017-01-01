from rest_framework import generics
from rest_framework  import mixins
from rest_framework import permissions

from app.api.libraries.customresponse import CustomResponse
from app.api.libraries.permissions import IsAuthenticatedOrCreate

class IndexView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    permission_classes = (permissions.AllowAny, )

    def get(self, request):
	payload = dict()
	payload["resp"] = "register or login"
	return CustomResponse(payload=payload)
