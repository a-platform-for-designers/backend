from api.views.user_views import UserProfileViewSet
from .views_common import CaseImageViewSet, CommentViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserProfileViewSet, basename='user')
router.register('caseimages', CaseImageViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
