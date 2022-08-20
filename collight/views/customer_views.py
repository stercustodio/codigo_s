from collight.models.customer import Customer
from collight.serializers import CustomerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets


class CustomerViewset(viewsets.ModelViewSet):
    
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = [
        'gender',
        'address',
        'name',
        'email',
        'birthdate',
        'marital_status'
        ]
    ordering_fields = ['name']
