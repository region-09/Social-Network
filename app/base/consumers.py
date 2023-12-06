import datetime
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from . models import User, Message, Friend
from django.db.models import Q
import re

class Chat(AsyncWebsocketConsumer):
    async def connect(self):
        print("connection!")
        room = self.scope['url_route']['kwargs']['room']
        await self.channel_layer.group_add(room, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        room = self.scope['url_route']['kwargs']['room']
        await self.channel_layer.group_discard(room, self.channel_name)

    # IMPORTANT 'send.message' is for function in line 27 "send_message" we replace by "."
    async def receive(self, text_data):
        room = self.scope['url_route']['kwargs']['room']
        data = json.loads(text_data)
        message = data['message']
        sender = data['sender']
        recipient = data['recipient']


        await self.save_message(sender, recipient, message)
        
        await self.channel_layer.group_send(
            room,
            {
                'sender': self.scope['user'].username,
                'type': 'send.message',
                'message': message,
            }
        )

    async def send_message(self, event):
        # Send the received message to the WebSocket
        if len(event) == 3:
            message = event['message']
            user = self.scope['user'].username
            sender = event['sender']
            if sender != user:
                await self.send(text_data=json.dumps(
                    {'sender': sender, 'message': message}))
            else:
                pass
    
    @sync_to_async
    def save_message(self, sender, recipient, message):
        user_sender = User.objects.get(username=sender)
        user_recipient = User.objects.get(username=recipient)
        Message.objects.create(sender=user_sender, recipient=user_recipient, message=message, timestamp=datetime.datetime.now())
        friendship = Friend.objects.filter(Q(user1=user_sender) | Q(user2=user_sender)).first()
        friendship.save()

class Notification(AsyncWebsocketConsumer):
    async def connect(self):
        print("Notification connection!")
        room = self.scope['url_route']['kwargs']['room']
        await self.channel_layer.group_add(room, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        room = self.scope['url_route']['kwargs']['room']
        await self.channel_layer.group_discard(room, self.channel_name)

    # IMPORTANT 'send.message' is for function in line 27 "send_message" we replace by "."
    async def receive(self, text_data):
        room = self.scope['url_route']['kwargs']['room']

        await self.channel_layer.group_send(
            room,
            {
                'sender': self.scope['user'].username,
                'type': 'send.message',
            }
        )

    async def send_message(self, event):
        # Send the received message to the WebSocket
        if len(event) == 2:
            user = self.scope['user'].username
            sender = event['sender']
            if sender != user:
                await self.send(text_data=json.dumps(
                    {'sender': sender, 'message': 'Received message'}))
            else:
                pass