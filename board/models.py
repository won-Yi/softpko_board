from django.db import models


class Board(models.Model):
    class Meta:
        db_table = "board"

    def __str__(self):
        return self.title
    
    title = models.CharField(max_length = 100)
    content = models.TextField()
    image = models.ImageField(upload_to = '%Y/%m', blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)