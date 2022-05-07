from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    owner = models.ForeignKey(User,
                              related_name='post_owner',
                              on_delete=models.CASCADE
                              )
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner}--{self.id}"


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image_post')
    image = models.ImageField()

    def __str__(self):
        return f"{self.post.title}--{self.post.id}--{self.id}"
