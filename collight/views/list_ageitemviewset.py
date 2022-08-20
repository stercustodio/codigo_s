



from collight.serializers.list_customer_serializers import ListCustomerSerializer
from collight.models.customer import Customer
from rest_framework import generics
from collight.models.order import Order
from collight.toolkit.customer_tools import OrderTools

class ListAgeItemViewSet(generics.ListAPIView):

    serializer_class = ListCustomerSerializer

    def get_queryset(self):
        queryset = Order.objects.all().
        for order in queryset:
            OrderTools.AgeFilter(item)
            customer.save()
        return queryset