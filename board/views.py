from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from board.models import Board
from .serializer import BoardListSerializer, BoardSerializer

class BoardView(APIView):
    def get(self, request):
        board_list = Board.objects.all()
        serializer = BoardListSerializer(board_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer= BoardSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)



class Board_detail(APIView):
    def get(self, request, board_id):
        board = get_object_or_404(Board, id = board_id)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def put(self, request, board_id):
        board = get_object_or_404(Board, id = board_id)
        serializer = BoardSerializer(board, data = request.data)
        # board는 원래 있던 글, data는 수정할 새로운 글.
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
             return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, board_id):
        board = get_object_or_404(Board, id = board_id)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)