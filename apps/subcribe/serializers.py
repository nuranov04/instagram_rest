from rest_framework import serializers
from apps.subcribe.models import Subscribe


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
        