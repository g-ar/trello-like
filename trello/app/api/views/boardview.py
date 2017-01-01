from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions

from app.models import Boards
from app.api.libraries.boardlib import BoardLib
from app.api.libraries.userlib import UserLib

from app.api.constants import *
from app.api.libraries.customresponse import CustomResponse

"""
{
  "board_name": "Hello"
}
"""

board_lib = BoardLib()
user_lib = UserLib()

class BoardView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    model = Boards
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, board_id=None):
        if board_id:
            vals = board_lib.get_board(board_ids=[board_id])
            if vals:
                return CustomResponse(message="Board details", payload=vals, code=HTTP_200_OK)
            else:
                return CustomResponse(message="Not found", code=HTTP_404_NOT_FOUND)
        else:
            board_ids = user_lib.get_board_id_list(request.user)
            vals = board_lib.get_board(board_ids=board_ids)
            return CustomResponse(message="Board details", payload=vals, code=HTTP_200_OK)

    def post(self, request):
        try:
            board_details = request.data
            board_id = board_lib.add_board(board_details, request.user)
            # user_lib.update_board_id_list(request.user, board_id)
            return CustomResponse(message="Board added", code=HTTP_201_CREATED)
        except Exception as e:
            return CustomResponse(message="Board could not be added: "+str(e), code=HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            board_details = request.data
            board_lib.update_board(board_details)
            return CustomResponse(message="Board updated", code=HTTP_200_OK)
        except Exception as e:
            return CustomResponse(message="Board could not be updated: "+str(e), code=HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            board_details = request.data
            board_lib.delete_board(board_details, request.user)
            return CustomResponse(message="Board deleted", code=HTTP_200_OK)
        except Exception as e:
            return CustomResponse(message="Board could not be deleted: "+str(e), code=HTTP_500_INTERNAL_SERVER_ERROR)
