from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='login.html')),
    path('user/profile/', TemplateView.as_view(template_name='profile.html')),
    path('user/rent', TemplateView.as_view(template_name='available_bikes.html')),
    path('user/ctrip/', TemplateView.as_view(template_name='current_rent.html')),
    path('user/history', TemplateView.as_view(template_name='payment.html')),
    path('user/balance', TemplateView.as_view(template_name='balance.html')),
    path('admin/bike', TemplateView.as_view(template_name='admin_product.html')),
    path('admin/maintain', TemplateView.as_view(template_name='admin_maintain.html')),
    path('admin/order', TemplateView.as_view(template_name='admin_order.html')),
    path('admin/side_menu', TemplateView.as_view(template_name='admin_side_menu.html')),
    path('admin/user', TemplateView.as_view(template_name='admin_user.html')),
    path('admin/visual', TemplateView.as_view(template_name='admin_visual.html')),
    path('user/login_side', TemplateView.as_view(template_name='login_side_menu.html')),
    path('user/maintain', TemplateView.as_view(template_name='maintain.html')),
    path('user/map', TemplateView.as_view(template_name='map.html')),
    path('user/title', TemplateView.as_view(template_name='nav_title.html')),
    path('user/passwd', TemplateView.as_view(template_name='password.html')),
    path('user/register', TemplateView.as_view(template_name='register_page.html')),
    path('user/top', TemplateView.as_view(template_name='top_nav.html')),
    path('user/about', TemplateView.as_view(template_name='tos.html')),
    path('user/menu', TemplateView.as_view(template_name='user_side_menu.html')),
    path('user/corder', TemplateView.as_view(template_name='corder.html')),
    path('user/rentmap', TemplateView.as_view(template_name='rentmap.html')),
    path('admin/', TemplateView.as_view(template_name='admin_login.html')),
    path('user/productlist', TemplateView.as_view(template_name='product_list.html')),
    path('user/shoppingcart', TemplateView.as_view(template_name='shopping_cart.html'))
]
