from collight.toolkit.customer_tools import CustomerTools
from collight.models.customer import Customer
from collight.models.order import Order
from collight.views.list_profilecustomer_views import ListCustomerViewSet

marcelopontocom = Customer.objects.get(pk='mar.valerio@hotmail.com')
a = CustomerTools.OrdersLog(marcelopontocom)
marcelo = Customer.objects.get(pk='mar.valerio@hotmail.com.br')
b = CustomerTools.OrdersLog(marcelo)


