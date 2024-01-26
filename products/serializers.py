from rest_framework import serializers
from .models import Product, Brand , ProductImages , Review
from taggit.serializers import TagListSerializerField,TaggitSerializer


class ProductImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['image']

    
class ProductReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user','review','rate','created_at']

class ProductListSerializer(TaggitSerializer,serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    tags = TagListSerializerField()


    class Meta:
        model = Product
        fields = ['name','brand','review_count','avg_rate','flag','price','image','sku','subtitle','description','tags']


class ProductDetailSerializer(TaggitSerializer,serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    images = ProductImagesSerializers(source='product_image',many=True)
    reviews = ProductReviewsSerializers(source = 'Review_product',many=True)
    tags = TagListSerializerField()
    class Meta:
        model = Product
        fields = ['name','brand','review_count','avg_rate','flag','price','image','sku','subtitle','description','images','reviews','tags']



    

class BrandListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'