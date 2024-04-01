from rest_framework import serializers
from .models import Customer

class CustomerSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'email', 'contact']