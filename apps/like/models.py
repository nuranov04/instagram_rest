from django.db import models
from apps.post.models import Post
from apps.user.models import User


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')

    def __str__(self):
        return f"{self.id}"