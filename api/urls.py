from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (CommentViewSet,
                    FollowViewSet,
                    GroupViewSet,
                    PostViewSet)

router_v1 = DefaultRouter()
router_v1.register('v1/posts',
                   PostViewSet,
                   basename='posts')
router_v1.register('v1/group',
                   GroupViewSet,
                   basename='groups')
router_v1.register('v1/follow',
                   FollowViewSet,
                   basename='follows')
router_v1.register(r'v1/posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('',
         include(router_v1.urls)),
    path('v1/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
]
