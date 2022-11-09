from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users import views


urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('mock/', views.mockView.as_view(), name='mock_view'),
    path('api/token/', views.CustomTokenObtainPariView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
