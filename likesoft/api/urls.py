from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from .views import BookViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
]
