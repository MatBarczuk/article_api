from django.urls import path
from rest_framework.routers import SimpleRouter

from posts import views

router = SimpleRouter()
router.register('v1/users', views.UserViewSet, basename='users')
router.register('v2/posts', views.PostViewSet, basename='posts')

urlpatterns = router.urls
