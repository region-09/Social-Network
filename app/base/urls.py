from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('chat/<str:room>', views.chat, name='chat'),
    path('chatting', views.friends_message_view, name='friends_message_view'),
    path('upload', views.upload, name='upload'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('requests', views.requests, name='requests'),
    path('people', views.people, name='people'),
    path('chatgpt', views.chatGPT, name='chatgpt'),
]