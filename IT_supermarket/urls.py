from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('docs/', include_docs_urls(title='API')),
    path('', include('templates.urls')),
    path('users/', include('users.urls')),
    path('goods/', include('goods.urls')),
    path('operations/', include('operations.urls')),
    path('orders/', include('orders.urls')),
    path('echart/', include('echarts.urls')),
]
