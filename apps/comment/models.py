from django.db import models
from apps.post.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    comment = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.id}--{self.id}"