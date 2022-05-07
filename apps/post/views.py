from rest_framework import viewsets
from apps.post.models import Post, PostImage
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.post.serializers import PostSerializer, PostImageSerializer


class PostAPIViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostImageAPIViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
