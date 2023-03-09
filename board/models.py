from django.db import models
from users.models import User

class Board(models.Model):
    class Meta:
        db_table = "board"

    def __str__(self):
        return self.title
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    image = models.ImageField(upload_to = '%Y/%m', blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



class Comment(models.Model):
    class Meta:
        db_table = "comment"

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    board = models.ForeignKey(Board,on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)