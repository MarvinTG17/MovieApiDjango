from django.urls import path,include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = routers.DefaultRouter()
router.register('',views.UserViewSet, basename='users')

urlpatterns = [
    path('api/', include(router.urls)),
    path('token/',TokenObtainPairView.as_view(),name='get_token'),
    path('refrest-token/',TokenRefreshView.as_view(),name='refresh_token')
]
