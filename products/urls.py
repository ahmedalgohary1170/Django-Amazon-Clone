from django.urls import path
from .views import ProductDetail,ProductList,BrandList,BrandDetail
from . import api



urlpatterns=[
    path('brands',BrandList.as_view() ),
    path('brands/<slug:slug>',BrandDetail.as_view()),
    path('', ProductList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),
    
    # api
    path('api/list' , api.ProductListAPI.as_view()),
    path('api/list/<int:pk>' , api.ProductDetailAPI.as_view()),

    path('api/Brands' , api.BrandListAPI.as_view()),
    path('api/Brands/<int:pk>', api.BrandDetailAPI.as_view()),
]