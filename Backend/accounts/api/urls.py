from django.urls import path
from . import views
from . views import MyTokenObtainPairView,AdminTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('',views.get_routes,name='api'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/token/', AdminTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]