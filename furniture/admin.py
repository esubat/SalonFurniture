from django.contrib import admin
from .models import Category , Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug' :('title',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'category' , 'price' , 'available']
    list_filter = ['name','price','category']
    prepopulated_fields = {'slug':('name',)}