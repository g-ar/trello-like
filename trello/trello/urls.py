"""trello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from app.api.views.index import IndexView
# from app.api.views.userview import UserView
from app.api.views.registerview import RegisterView
# from app.api.views.tokenview import TokenView
from app.api.views.loginview import LoginView
from app.api.views.boardview import BoardView
from app.api.views.listview import ListView
from app.api.views.cardview import CardView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^board/(?P<board_id>[0-9]+)/$', BoardView.as_view()),
    url(r'^board/$', BoardView.as_view()),
    url(r'^list/(?P<list_id>[0-9]+)/$', ListView.as_view()),
    url(r'^list/$', ListView.as_view()),
    url(r'^card/(?P<card_id>[0-9]+)/$', CardView.as_view()),
    url(r'^card/$', CardView.as_view()),
]
