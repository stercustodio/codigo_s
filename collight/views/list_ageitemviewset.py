# from collight.serializers.list_customer_serializers import ListCustomerSerializer
# from collight.models.customer import Customer
# from rest_framework import generics
# from collight.models.order import Order
# from collight.toolkit.customer_tools import OrderTools

# class ListAgeItemViewSet(generics.ListAPIView):

#     serializer_class = ListCustomerSerializer

#     def get_queryset(self):
#         queryset = Order.objects.all().
#         for order in queryset:
#             OrderTools.AgeFilter(item)
#             customer.save()
#         return queryset

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collight.models.order import Order
from collight.models.customer import Customer
from collight.serializers.order_serializers import OrderSerializer
from collight.toolkit.order_tools import OrderTools

@api_view(['GET'])
def ageitemview(request, product):  
    if request.method == 'GET':
        return Response(OrderTools.AgeFilter(product))