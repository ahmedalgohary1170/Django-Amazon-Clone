from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


from products.models import Product
from utils.generate_code import generate_code
from accounts.models import Address



ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered')
)


class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_owner',on_delete=models.SET_NULL,blank=True, null=True)
    status = models.CharField( choices=ORDER_STATUS,max_length=20)
    code = models.CharField(default=generate_code , max_length=20)
    order_time = models.DateTimeField(default = timezone.now)
    delivary_time = models.DateTimeField(blank=True, null=True)
    delivary_address = models.ForeignKey(Address,related_name='delivary_address',on_delete=models.SET_NULL,blank=True, null=True)
    coupon = models.ForeignKey('Coupon',related_name='order_coupon',on_delete=models.SET_NULL,blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    total_with_coupon = models.FloatField(blank=True, null=True)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name = 'order_detail',on_delete = models.CASCADE)
    product = models.ForeignKey(Product,related_name = 'orderdetail_product',on_delete = models.SET_NULL,blank=True, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField(blank=True, null=True)



CART_STATUS = (
    ('Inprogress','Inprogress'),
    ('Completed','Completed'),

)



class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart_owner',on_delete=models.SET_NULL,blank=True, null=True)
    status = models.CharField( choices=CART_STATUS,max_length=20)
    coupon = models.ForeignKey('Coupon',related_name='cart_coupon',on_delete=models.SET_NULL,blank=True, null=True)
    total_with_coupon = models.FloatField(blank=True, null=True)

class CartDetail(models.Model):
    order = models.ForeignKey(Cart,related_name = 'cart_detail',on_delete = models.CASCADE)
    product = models.ForeignKey(Product,related_name = 'cartdetail_product',on_delete = models.SET_NULL,blank=True, null=True)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(blank=True, null=True)


class Coupon(models.Model):
    code = models.CharField(max_length=20)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    quantity = models.IntegerField()
    descount = models.FloatField()
    def save(self, *args, **kwargs):
       week = datetime.timedelta(days=7) 
       self.end_date=self.start_date + week
       super(Coupon, self).save(*args, **kwargs) # Call the real save() method