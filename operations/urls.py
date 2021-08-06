from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from operations.views import AccountView, PayView, AddressViewSet

app_name = 'operation'

router = DefaultRouter()
router.register(r'address', AddressViewSet, basename='address')

urlpatterns = [
    url(r'^', include(router.urls)),
    path('account/', AccountView.as_view(), name='account'),
    path('pay/<int:pk>/', PayView.as_view(), name='pay'),

]
