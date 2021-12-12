from django.urls import path, include
from .views import CreateRoomView, GetRoom, JoinRoom, RoomView
urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
]
