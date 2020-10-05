from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import UserLoginView

urlpatterns = [
    # user login API
    path('login/', UserLoginView.as_view(), name='user_login'),
    # user token refresh API
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='user_token_refresh'),
]
