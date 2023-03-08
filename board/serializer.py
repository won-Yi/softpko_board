from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('title', 'content', 'image')


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"