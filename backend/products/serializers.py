from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',   # reference to property of model, it could be an instance method, it could be a property
            'my_discount'  # reference to instance method
        ]
        
    def get_my_discount(self, obj):
        print(obj.id)
        return obj.get_discount()