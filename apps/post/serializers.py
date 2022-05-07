from rest_framework import serializers
from apps.post.models import Post, PostImage
from apps.like.serializers import LikeSerializer


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    image_post = PostImageSerializer(read_only=True, many=True)
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_total_likes(self, instance):
        return instance.post_like.all().count()

