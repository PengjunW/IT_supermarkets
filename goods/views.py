# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from goods.filters import GoodsFilter
from goods.models import Goods
from goods.serializers import GoodsSerializers


class GoodsListView(ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers

    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]

    # filter class
    filter_class = GoodsFilter
    search_fields = ('goods_name', 'goods_brief_description')
    # order by attribute
    ordering_fields = ('price',)


class GoodsUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = GoodsSerializers
    queryset = Goods.objects.all()
