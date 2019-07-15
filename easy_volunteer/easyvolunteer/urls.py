from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('introduce', views.introduce, name='introduce'),
    path('select', views.select, name='select'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('mypage', views.mypage, name='mypage'),
    path('quest', views.quest, name='quest'),
    path('point', views.point, name='point'),
]