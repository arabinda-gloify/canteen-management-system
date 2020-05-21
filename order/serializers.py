from rest_framework import serializers
from order.models import Order, OrderItem, Item




class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        # fields = ['id', 'timestamp', 'item', 'active', 'price', 'url']
        fields = '__all__'


# class OrderItemSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = OrderItem
#         # fields = ['id', 'item', 'price', 'url',]
#         fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        # fields = ['id', 'item', 'price', 'url',]
        fields = '__all__'
