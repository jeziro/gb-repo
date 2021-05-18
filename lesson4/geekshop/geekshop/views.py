from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def main(request):
    products = Product.objects.all()[:4]

    context = {
        'slogan': 'СУПЕР УДОБНЫЕ СТУЛЬЯ',
        'topic': 'ТРЕНДЫ',
        'products': products,
    }
    return render(request, 'index.html', context=context)

def contact(request):
    return render(request, 'contact.html')