from rest_framework import generics
from rest_framework  import mixins
from rest_framework  import permissions

from app.api.constants import *
from app.api.libraries.customresponse import CustomResponse

from app.api.libraries.listlib import ListLib
from app.models import Lists

"""
{
    "list_name": "alist",
    "card_ids": [1, 2]
}
"""

list_lib = ListLib()

class ListView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    model = Lists
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, list_id=None):
        if list_id:
            payload = list_lib.get_list(list_ids=[int(list_id)])
        else:
            payload = list_lib.get_list_from_user_board(user=request.user)

        return CustomResponse(message="List details" , payload=payload, code=HTTP_200_OK)

    def post(self, request):
        try:
            list_details = request.data
            list_lib.add_list(list_details)
            return CustomResponse(message="List added", code=HTTP_201_CREATED)

        except Exception as e:
            return CustomResponse(message="Could not add list: "+str(e), code=HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        modifications = request.data
        list_lib.update_list(list_details=modifications)
        return CustomResponse(message="List updated", code=HTTP_200_OK)

    def delete(self, request):
        try:
            list_ids = request.data.get(LIST_IDS)
            board_id = request.data.get(BOARD_ID)
            list_lib.delete_list(list_ids=list_ids)
            upd_list_ids = board_lib.get_lists_list(board_id=board_id)

            for l in list_ids:
                upd_list_ids.remove(l)

            board_details = {BOARD_ID: board_id, LIST_IDS: upd_list_ids}
            board_lib.update_board(board_details)
            return CustomResponse(message="Lists deleted", code=HTTP_200_OK)

        except Exception as e:
            return CustomResponse(message=str(e), code=HTTP_500_INTERNAL_SERVER_ERROR)
