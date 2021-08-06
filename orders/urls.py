from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from django.urls import path
from orders.views import OrderViewSet, ShoppingCartViewset,MangageOrder,OrderDelete


app_name = 'order'

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'shoppingCart', ShoppingCartViewset, basename='shoppingCart')

urlpatterns = [
    url(r'^', include(router.urls)),
    path('manage/', MangageOrder.as_view(), name='manage'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),

]
