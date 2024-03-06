from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
import datetime


from .serializers import OrderSerializer,OrderdetailSerializer,CartSerializer,CartdetailSerializer
from .models import Order,OrderDetail,Cart,CartDetail,Coupon
from products.models import Product
from settings.models import DeliveryFee


class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = super(OrderListAPI, self).get_queryset()

        user = User.objects.get(username=self.kwargs['username'])

        queryset = queryset.filter(user=user)
        return queryset
    

class OrderDatailAPI(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class ApplyCouponAPI(generics.GenericAPIView):
    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        coupon = get_object_or_404(Coupon,code=request.data['coupon_code'])
        cart = Cart.objects.get(user=user,status='Inprogress')
        deliveryFee = DeliveryFee.objects.last().fee
        if coupon and coupon.quantity > 0:
            today_date = datetime.datetime.today().date()

            if today_date >=coupon.start_date and today_date <= coupon.end_date:
                coupon_value = round(cart.cart_total / 100*coupon.descount,2)
                sub_total = cart.cart_total - coupon_value

                cart.coupon = coupon
                cart.total_with_coupon = sub_total
                cart.save()
                coupon.quantity -= 1
                coupon.save()
                return Response({'massage':'coupon was applied succesfully'})
            else:
                return Response({'massage':'coupon is invalid or expired'})
        
        return Response({'massage':'coupon not found'})