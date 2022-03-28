from django.shortcuts import render
from rest_framework.response import Response

from .models import ChatRoom
from .serializers import ChatSerializer, RoomsSerializer
from rest_framework.views import APIView


class ChatView(APIView):
    def get(self, request, pk):

        try:
            room = ChatRoom.objects.get(id=pk)
        except:
            room = None
        if room is None:
            room = ChatRoom()
            room.save()

        serializer = ChatSerializer(room)
        return Response(serializer.data)


class MyChatsView(APIView):
    def get(self, request):

        rooms = ChatRoom.objects.filter(client=request.user)
        serializer = RoomsSerializer(rooms, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)

