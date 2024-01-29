from django.shortcuts import render , get_object_or_404
from .models import Product , Category
from django.views import View

from cart.forms import CartAddForm


class ProductListView(View):
    
    def get(self , request , category_slug = None ):
        products = Product.objects.filter(available = True)
        category = None
        categories = Category.objects.all()
        if category_slug:
            category = get_object_or_404(Category , slug = category_slug)
            products = products.filter(category = category)
        context = {
            'products':products,
            'categories' : categories,
            }
        return render( request , 'furniture/list.html' , context)

class ProductDetailView(View):
    
    def get(self,request , id ):

        cart_form = CartAddForm()
        product = get_object_or_404(Product ,
                                     id=id , 
                                     available = True)
                
        context ={'product':product,
                  'cart_form':cart_form}
        return render(request , 'furniture/detail.html' , context)