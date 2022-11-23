from django.db import models
from users.models import User


class Inquiry(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Comment(models.Model) :
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    inquiry = models.ForeignKey(Inquiry, on_delete = models.CASCADE, related_name="comment_set")
    cmt_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)