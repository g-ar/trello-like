from app.api.constants import *
from app.models import Users, Boards, Lists, Cards
from app.api.helpers import validators

import json

class CardLib():
    def get_card(self, card_ids):
        if card_ids:
            cobj = Cards.objects.filter(card_id__in=card_ids).values()
            cards = []

            for c_id in card_ids:
                cards += [{CARD_ID: c[CARD_ID],
                           CARD_NAME: c[CARD_NAME],
                           CARD_DESC: c[CARD_DESC],
                           CARD_DUE_DATE: c[CARD_DUE_DATE],
                           CARD_STATUS: c[CARD_STATUS]} for c in cobj if c[CARD_ID] == c_id]

            return cards
        else:
            return []

    def get_cards_from_user_board(self, user):
        uobj = Users.objects.filter(user_name=user).values()[0]
        board_list = json.loads(uobj.get(BOARD_IDS))
        list_ids = []

        for b_id in board_list:
            bobj = Boards.objects.filter(board_id=b_id).values()[0]
            list_ids += json.loads(bobj.get(LIST_IDS))
            
        card_ids = []
        if list_ids:
            for l_id in list_ids:
                lobj = Lists.objects.filter(list_id=l_id).values()[0]
                card_ids += json.loads(lobj.get(CARD_IDS))

        cards = []
        if card_ids:
            cobj = Cards.objects.filter(card_id__in=card_ids).values()
            
            for c_id in card_ids:
                cards += [{CARD_ID: c[CARD_ID],
                           CARD_NAME: c[CARD_NAME],
                           CARD_DESC: c[CARD_DESC],
                           CARD_DUE_DATE: c[CARD_DUE_DATE],
                           CARD_STATUS: c[CARD_STATUS]} for c in cobj if c[CARD_ID] == c_id]
            return cards
        else:
            return []

    def add_card(self, card_details):
        list_id = card_details[LIST_ID]
        del card_details[LIST_ID]
        card_id = Cards.objects.create(**card_details).card_id
        card_ids = json.loads(Lists.objects.filter(list_id=list_id).values()[0].get(CARD_IDS))
        card_ids.append(card_id)
        dct = {CARD_IDS: card_ids}
        Lists.objects.filter(list_id=list_id).update(**dct)
        return card_id

    def update_card(self, card_details):
        Cards.objects.filter(card_id=card_details[CARD_ID]).update(**card_details)

    def delete_card(self, card_ids):
        Cards.objects.filter(card_id__in=card_ids).delete()

