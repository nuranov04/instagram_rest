from rest_framework.routers import DefaultRouter
from apps.post.views import PostAPIViewSet, PostImageAPIViewSet


routers = DefaultRouter()
routers.register('posts', PostAPIViewSet, basename='posts')
routers.register('post_images', PostImageAPIViewSet, basename='post_images')

urlpatterns = routers.urls
