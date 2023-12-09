# models.py
from django.db import models
   
class Comment(models.Model):
    user_name = models.CharField(max_length=255)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article_url = models.URLField(null=True)

    def __str__(self):
        return f'{self.user_name} - {self.created_at}'
