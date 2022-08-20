from collight.serializers.list_customer_serializers import ListCustomerSerializer
from collight.models.customer import Customer
from rest_framework import generics
from collight.toolkit.customer_tools import CustomerTools

class ListProfileCustomerViewSet(generics.ListAPIView):

    serializer_class = ListCustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()
        for customer in queryset:
            customer.profile = CustomerTools.PerfilCustomer(customer)
            customer.save()
        return queryset
