from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer


class CommentApiViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

