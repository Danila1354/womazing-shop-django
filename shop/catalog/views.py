from django.shortcuts import render

# Create your views here.
from .models import ProductVariant, Category

def catalog(request):
    products= ProductVariant.objects.select_related('product','color','category').all()
    categories = Category.objects.all()
    return render(request,'catalog/catalog.html',{'products':products, 'categories':categories})