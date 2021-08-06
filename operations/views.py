from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response

from operations.serializers import UserAccountSerializer, AddressSerializer
from orders.models import Orders
from goods.models import Goods
from .models import UserAddress


class AccountView(RetrieveUpdateAPIView):
    serializer_class = UserAccountSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get_object(self):
        return self.request.user


class PayView(UpdateAPIView):
    serializer_class = UserAccountSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get_object(self):
        return self.request.user

    def update(self, request, pk):
        order = Orders.objects.get(id=pk)

        user = self.request.user
        # good = Goods.objects.get(goods_id=order.good)
        # total = order.nums * good.price
        if user.account_balance >= order.charge:
            user.account_balance -= order.charge
            order.order_status = 1
            user.save()
            order.save()
            return Response({
                'msg': 'success',
                'results': {
                    'order_id': order.order_id,
                    'order_status': order.order_status
                }
            })
        else:
            order.order_status = 2
            user.save()
            order.save()
            return Response({
                'msg': 'fail',
                'results': {
                    'order_id': order.order_id,
                    'order_status': order.order_status
                }
            })


class AddressViewSet(viewsets.ModelViewSet):
    """
    Address management
    list:
        get address
    create:
        add address
    update:
        Update address
    delete:
        delete address
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = AddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
