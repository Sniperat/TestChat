from rest_framework import serializers
from .models import ChatRoom, Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)

    class Meta:
        model = ChatRoom
        fields = '__all__'


class RoomsSerializer(serializers.ModelSerializer):
    last_message = MessageSerializer()

    class Meta:
        model = ChatRoom
        fields = ('id', 'client', 'doktor', 'last_message', 'created_at')
