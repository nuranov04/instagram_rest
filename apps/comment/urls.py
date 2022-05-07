from rest_framework.routers import DefaultRouter
from apps.comment.views import CommentApiViewSet

routers = DefaultRouter()
routers.register('', CommentApiViewSet, basename='comment')

urlpatterns = routers.urls
