from app.api.constants import *
from app.models import Users, Token, Boards
from app.api.helpers import validators

import json

class BoardLib():
    def get_board(self, board_ids):
        if board_ids:
            brdname = Boards.objects.filter(board_id__in=board_ids).values()
            return brdname
        else:
            return []

    def get_lists_list(self, board_id):
        bobj = Boards.objects.filter(board_id=board_id).values()[0]
        lists_list = json.loads(bobj.get(LIST_IDS))
        return lists_list

    def add_board(self, board_details, user):
        if not board_details.get(LIST_IDS):
            board_details[LIST_IDS] = []
        board_id = Boards.objects.create(**board_details).board_id
        board_ids = json.loads(Users.objects.filter(user_name=user).values()[0].get(BOARD_IDS))
        board_ids.append(board_id)
        dct = {BOARD_IDS: board_ids}
        Users.objects.filter(user_name=user).update(**dct)
        return board_id
    
    def update_board(self, board_details):
        Boards.objects.filter(board_id=board_details[BOARD_ID]).update(**board_details)

    def delete_board(self, board_details, user):
        bobj = Users.objects.filter(user_name=user).values()[0]
        board_ids = json.loads(bobj.get(BOARD_IDS))
        del_board_ids = board_details[BOARD_IDS]

        for b_id in board_ids:
            board_ids.remove(b_id)

        Boards.objects.filter(board_id__in=del_board_ids).delete()

