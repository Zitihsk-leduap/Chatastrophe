from django.urls import path
from .consumers import *
 
  # The consumers file is just like a view file for websocket connections

websocket_urlpatterns =[
  path("ws/chatroom/<chatroom_name>",ChatroomConsumer.as_asgi()),
]