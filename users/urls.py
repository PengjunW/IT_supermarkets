from django.urls import path

from users.views import UserDetailView, UserLoginView, UserRegisterView, UserUpdateView, UserListView, UserDelete

app_name = 'users'

urlpatterns = [
    path('detail/', UserDetailView.as_view(), name='detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('list/', UserListView.as_view(), name='list'),
    path('delete/<int:pk>/', UserDelete.as_view(), name='delete'),
]
