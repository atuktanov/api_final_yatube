from django.urls import include, path

from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'
router = SimpleRouter()
router.register('posts', PostViewSet)
router.register(
    r'^posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet)
urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
