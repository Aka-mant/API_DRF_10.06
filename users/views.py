from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import User
from .user_serializers import UserSerializer, UserCreateSerializer, UserTokenObtainSerializer, UserUpdateSerializer
from sections.permitions import IsModerator, IsSuperuser
from django.shortcuts import render

def api_docs_home(request):
    return render(request, "chuse_doc_ui.html")

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsSuperuser]



class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return User.objects.filter(id=user.id).first()


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsSuperuser, ]

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainSerializer
    permission_classes = [AllowAny]


