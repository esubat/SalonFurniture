from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    category = models.ForeignKey(Category ,
                                 related_name='Products',
                                 on_delete=models.CASCADE)
    
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='furnitures',
                              blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
     
        
    def __str__(self) :
        return  self.name
    
    def get_absolute_url(self):
        return reverse('furniture:product-detail',
                       args=[self.id])
    class Meta:
        ordering =['-created']
       