from rest_framework import serializers
from .models import Cart,CartDetail,Order,OrderDetail

class CartdetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartDetail
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartdetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'

class OrderdetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_detail=OrderdetailSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'

