from django.contrib import admin
from .models import Product,ProductImages,Brand,Review
from modeltranslation.admin import TranslationAdmin

class ProductImagesInline(admin.TabularInline):
    model = ProductImages


    

class ProductAdmin(TranslationAdmin):
    inlines=[ProductImagesInline]
    list_display = ['id','name','review_count','avg_rate']




admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)