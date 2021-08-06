from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, ListAPIView, \
    RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from users.models import Users
from users.serializer import UserSerializer, UserRegisterSerializer, UserLoginSerializer, UserUpdateSerializer


class UserRegisterView(CreateAPIView):
    """
    register
    """
    queryset = Users.objects.all()
    serializer_class = UserRegisterSerializer


class UserLoginView(CreateAPIView):
    """
    login
    """
    queryset = Users.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            user = Users.objects.get(username=username)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({
                'msg': 'success',
                'results': {
                    'username': user.username,
                    'user_id': user.id,
                    'token': token
                }
            })
        else:
            return Response({
                'msg': 'fail',
                'results': {
                    'info': serializer.errors
                }
            })


class UserDetailView(RetrieveAPIView):
    """
    show detailed info
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserUpdateView(RetrieveUpdateAPIView):
    """
    update user's password
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user


class UserListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = UserSerializer
    queryset = Users.objects.all()


class UserDelete(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = UserSerializer
    queryset = Users.objects.all()
