from django.shortcuts import render , redirect
from django.views.generic import ListView,DetailView
from .models import Product,Brand,Review,ProductImages
from .tasks import execute_somthing
from django.db.models.aggregates import Count
from django.views.decorators.cache import cache_page

from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q


@cache_page( 60 * 1 )
def mydebug(request):
    # data = Product.objects.all()
    execute_somthing.delay()
    return render(request,'products/debug.html',{})




class ProductList(ListView):
    model=Product
    paginate_by = 50

    def get_queryset(self):
        # الحصول على قيمة السعر من طلب HTTP
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        # فلترة المنتجات حسب السعر
        if min_price and max_price:
            products = self.model.objects.filter(Q(price__gte=min_price) & Q(price__lte=max_price))
        elif min_price:
            products = self.model.objects.filter(price__gte=min_price)
        elif max_price:
            products = self.model.objects.filter(price__lte=max_price)
        else:
            products = self.model.objects.all()

        return products




class ProductDetail(DetailView):
    model=Product
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["images"] = ProductImages.objects.filter(product=self.get_object())
        context["related"] = Product.objects.filter(brand=self.get_object().brand)
        return context
    


class BrandList(ListView):
    model=Brand
    paginate_by = 50
    queryset = Brand.objects.annotate(product_count=Count('Product_brand'))


class BrandDetail(ListView):
    model=Product
    template_name='products/brand_detail.html'
    paginate_by = 1
    
    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        queryset=super().get_queryset().filter(brand=brand)
        return queryset


    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('Product_brand'))[0]
        return context


def add_review(request,slug):
    product = Product.objects.get(slug=slug)
    review = request.POST['review'] 
    rate = request.POST['rating']
    
    # add review

    Review.objects.create(
        user = request.user,
        product = product,
        review = review,
        rate = rate
    )

    reviews = Review.objects.filter(product=product)
    page= render_to_string('includes/reviews.html',{'reviews':reviews})
    return JsonResponse({'result':page})

