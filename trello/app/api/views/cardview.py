from rest_framework import generics
from rest_framework  import mixins
from rest_framework  import permissions

from app.api.constants import *
from app.api.libraries.customresponse import CustomResponse

from app.api.libraries.cardlib import CardLib
from app.models import Cards


"""
{
    "card_name": "alist",
    "card_desc": "a lengthy description",
    "card_due_date": ..,
    "card_status": false,
    "list_id": 1
}
"""
card_lib = CardLib()

class CardView( generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    model = Cards
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, card_id=None):
        if card_id:
            payload = card_lib.get_card(card_ids=[int(card_id)])
        else:
            payload = card_lib.get_cards_from_user_board(user=request.user)
        return CustomResponse(message="Card details" , payload=payload, code=HTTP_200_OK)

    def post(self, request):
        try:
            card_details = request.data
            card_lib.add_card(card_details)
            return CustomResponse(message="Card added", code=HTTP_201_CREATED)
        except Exception as e:
            return CustomResponse(message="Could not add card: "+str(e), code=HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        modifications = request.data
        card_lib.update_card(card_details=modifications)
        return CustomResponse(message="Card updated", code=HTTP_200_OK)

    def delete(self, request):
        try:
            card_ids = request.data.get(CARD_IDS)
            list_id = request.data.get(LIST_ID)
            card_lib.delete_card(card_ids=card_ids)
            upd_card_ids = list_lib.get_card_list(list_id=list_id)
            for c in card_ids:
                upd_card_ids.remove(c)
            list_details = {LIST_ID: list_id, CARD_IDS: upd_card_ids}
            list_lib.update_list(list_details)
            return CustomResponse(message="Cards deleted", code=HTTP_200_OK)
        except Exception as e:
            return CustomResponse(message=str(e), code=HTTP_500_INTERNAL_SERVER_ERROR)
