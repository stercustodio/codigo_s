"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from collight.views.customer_views import CustomerViewset
from collight.views.list_profilecustomer_views import ListProfileCustomerViewSet
from collight.views.order_views import OrderViewset
from collight.views.list_ageitemviewset import ageitemview
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewset)
router.register(r'order', OrderViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('user/customerprofile/', ListProfileCustomerViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('faixa/<pk>', ageitemview)
]
