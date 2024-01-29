from django.urls import path
from .views import cart_add , cart_remove , cart_view

app_name = 'cart'

urlpatterns = [
    path('', cart_view , name='cart_view'),
    path('add/<int:id>', cart_add , name='cart_add'),
    path('remove/<int:id>' , cart_remove , name='cart_remove')
]