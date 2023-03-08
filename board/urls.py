from django.urls import path, include
from board import views

urlpatterns = [
    path('',views.BoardView.as_view(), name='boardview'),
    path('<int:board_id>/', views.Board_detail.as_view(), name ="board_detail"),
]
