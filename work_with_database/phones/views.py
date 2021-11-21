from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    param = request.GET.get('sort')
    if param == 'name':
        sorted_objects = Phone.objects.order_by('name')
    elif param == 'min_price':
        sorted_objects = Phone.objects.order_by('price')
    elif param == 'max_price':
        sorted_objects = Phone.objects.order_by('-price')
    else:
        sorted_objects = Phone.objects.all()

    context = {
        'phones': sorted_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone = None
    if slug == 'samsung-galaxy-edge-2':
        phone = Phone.objects.all()[0]
    if slug == 'iphone-x':
        phone = Phone.objects.all()[1]
    elif slug == 'nokia-8':
        phone = Phone.objects.all()[2]

    context = {
        'phone': phone
    }
    return render(request, template, context)
