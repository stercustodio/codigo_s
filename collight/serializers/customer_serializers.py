from collight.models.customer import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):  
    class Meta():
       model = Customer
       fields = '__all__'
       read_only_fields = ('profile',)
