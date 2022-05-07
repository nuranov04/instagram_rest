from rest_framework.routers import DefaultRouter
from apps.like.views import LikeApiViewSet

routers = DefaultRouter()
routers.register('', LikeApiViewSet, basename='like')

urlpatterns = routers.urls
