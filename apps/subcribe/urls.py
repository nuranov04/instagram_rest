from rest_framework.routers import DefaultRouter

from apps.subcribe.views import SubscribeViewSet

router = DefaultRouter()
router.register('', SubscribeViewSet, basename='subscribe')

urlpatterns = router.urls