from collight.models.order import Order
from collight.serializers import OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets


class OrderViewset(viewsets.ModelViewSet):
    
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = [
        'status',
        'customer'
        'items',
        'closed',
        'created_at'
    ]    
    ordering_fields = ['customer']