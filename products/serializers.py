from rest_framework import serializers
from .models import Product,Brand

class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count= serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_review_count(self,object):
        review= object.Review_product.all().count()
        return review

class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'




class BrandListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'