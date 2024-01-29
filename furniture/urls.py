from django.urls import path
from .views import ProductListView , ProductDetailView


app_name = 'furniture'
urlpatterns = [
    path('',ProductListView.as_view(), name='all-products'),
    path('<int:id>/',ProductDetailView.as_view() , name='product-detail')
]