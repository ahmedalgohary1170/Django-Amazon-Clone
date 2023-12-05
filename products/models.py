from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

FLAG_TYPES =(
    ('New','New'),
    ('sale','sale'),
    ('feature','feature')
)



class Product(models.Model):
    name = models.CharField(max_length=120)
    flag = models.CharField(max_length=10,choices=FLAG_TYPES)
    price = models.FloatField()
    image = models.ImageField(upload_to='product')
    sku = models.IntegerField()
    subtitle = models.TextField(max_length=500)
    description = models.TextField(max_length=50000)
    brand = models.ForeignKey('Brand',related_name='Product_brang',on_delete=models.SET_NULL,null=True)
    tags = TaggableManager()


    slug = models.SlugField(blank=True,null=True)

    def save(self, *args, **kwargs):
        self.slug =slugify(self.name)
        super(Product).save(*args, **kwargs)



class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimages')



class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')
    slug = models.SlugField(blank=True,null=True)

    def save(self, *args, **kwargs):
        self.slug =slugify(self.name)
        super(Product).save(*args, **kwargs)


class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,related_name='Review_product',on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rate = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    created_at = models.DateTimeField(default=timezone.now)
