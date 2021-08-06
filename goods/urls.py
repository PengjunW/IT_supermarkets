from django.urls import path

from goods.views import GoodsListView, GoodsUpdateView

app_name = 'goods'

urlpatterns = [
    path('lists/', GoodsListView.as_view(), name='list'),
    path('update/<int:pk>/', GoodsUpdateView.as_view(), name='update')
]
