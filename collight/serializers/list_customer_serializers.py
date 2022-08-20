from collight.models.customer import Customer
from rest_framework import serializers


class ListCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        """Sets the Account as the model used on this serializer, and establishes
        the fields that are shown in the serialized result"""

        model = Customer
        fields = ('email', 'name', 'profile')