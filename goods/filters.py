import django_filters

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    # two parameters,
    # name is the filter, look up is the action,larger or less
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']
