from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .apps import UsersConfig
from .views import UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDeleteAPIView, UserTokenObtainPairView



app_name = UsersConfig.name


urlpatterns = [
    #users.urls
    path('', UserListAPIView.as_view(), name='user_list'),
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteAPIView.as_view(), name='user_delete'),

    # token urlpatterns
    
    path('token/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
