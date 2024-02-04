from django.shortcuts import render
from products.models import Product,Brand,Review
from django.db.models import Count
# Create your views here.
def home(request):
    new_product = Product.objects.filter(flag='New')[:10]
    sale_product = Product.objects.filter(flag='sale')[:10]
    feature_product = Product.objects.filter(flag='feature')[:6]
    brands = Brand.objects.annotate(product_count=Count('Product_brand'))[:10]
    reviews = Review.objects.all()
    return render(request,'settings/home.html',{
        'new_product':new_product,
        'sale_product':sale_product,
        'feature_product':feature_product,
        'brands':brands,
        'reviews':reviews

    })
