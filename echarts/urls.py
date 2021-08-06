from django.urls import path

from echarts import views

app_name = 'echart'

urlpatterns = [
    path('day_user/', views.Day_userView.as_view(), name='day_user'),
    path(r'season_order/', views.Season_orderView.as_view(), name='season_order'),
    path(r'user_number/', views.User_numberView.as_view(), name='user_number'),
    path(r'goods_number/', views.Goods_numberView.as_view(), name='goods_number'),
    path(r'order_number/', views.Order_numberView.as_view(), name='order_number'),
    path(r'day_order/', views.Day_orderView.as_view(), name='day_order'),
    path(r'season_user/', views.Season_userView.as_view(), name='season_user'),

]
