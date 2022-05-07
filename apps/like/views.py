from rest_framework import viewsets


from apps.like.serializers import LikeSerializer
from apps.like.models import Like


class LikeApiViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
