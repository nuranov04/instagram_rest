from rest_framework import serializers
from apps.like.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

