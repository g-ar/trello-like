from app.api.constants import *
from app.models import Users, Boards, Lists
from app.api.helpers import validators

import json


class ListLib():
    def get_list(self, list_ids):
        if list_ids:
            lobj = Lists.objects.filter(list_id__in=list_ids).values()
            lists = []

            for l_id in list_ids:
                lists += [{LIST_ID: l[LIST_ID], LIST_NAME: l[LIST_NAME], CARD_IDS: l[CARD_IDS]} for l in lobj if l[LIST_ID] == l_id]

            return lists
        else:
            return []

    def get_list_from_user_board(self, user): # all list id and names belonging to a user
        uobj = Users.objects.filter(user_name=user).values()[0]
        board_list = json.loads(uobj.get(BOARD_IDS))
        list_ids = []

        for b_id in board_list:
            bobj = Boards.objects.filter(board_id=b_id).values()[0]
            list_ids += json.loads(bobj.get(LIST_IDS))

        if list_ids:
            lobj = Lists.objects.filter(list_id__in=list_ids).values()
            lists = []

            for l_id in list_ids:
                lists += [{LIST_ID: l[LIST_ID], LIST_NAME: l[LIST_NAME], CARD_IDS: l[CARD_IDS]} for l in lobj if l[LIST_ID] == l_id]

            return lists
        else:
            return []

    def get_card_list(self, list_id):
        lobj = Lists.objects.filter(list_id=list_id).values()[0]
        card_list = json.loads(lobj.get(CARD_IDS))
        return card_list
        
    def add_list(self, list_details):
        board_id = list_details[BOARD_ID]
        del list_details[BOARD_ID]

        if not list_details.get(CARD_IDS):
            list_details[CARD_IDS] = []

        list_id = Lists.objects.create(**list_details).list_id
        list_ids = json.loads(Boards.objects.filter(board_id=board_id).values()[0].get(LIST_IDS))
        list_ids.append(list_id)
        dct = {LIST_IDS: list_ids}
        Boards.objects.filter(board_id=board_id).update(**dct)
        return list_id
    
    def update_list(self, list_details):
        Lists.objects.filter(list_id=list_details[LIST_ID]).update(**list_details)
        
    def delete_list(self, list_ids):
        Lists.objects.filter(list_id__in=list_ids).delete()

