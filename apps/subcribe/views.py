from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.subcribe.models import Subscribe
from apps.subcribe.serializers import SubscriberSerializer



class SubscribeViewSet(viewsets.ModelViewSet):
    queryset = Subscribe.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]