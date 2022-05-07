from rest_framework.routers import DefaultRouter
from apps.user.views import UserAPIViewSet

routers = DefaultRouter()

routers.register('', UserAPIViewSet, basename='user')

urlpatterns = routers.urls
