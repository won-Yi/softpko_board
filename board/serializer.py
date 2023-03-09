from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()
    def get_username(self,obj):
        return obj.user.username

    class Meta:
        model = Board
        fields = "__all__"


class BoardListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    

    def get_username(self,obj):
        return obj.user.username
    

    class Meta:
        model = Board
        fields = "__all__"