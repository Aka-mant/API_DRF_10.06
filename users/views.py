from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import User
from .user_serializers import UserSerializer, UserCreateSerializer, UserTokenObtainSerializer, UserUpdateSerializer



class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [AllowAny]

    # def get_object(self):
    #     user = self.request.user
    #     return User.objects.filter(id=user.id).first()


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainSerializer


