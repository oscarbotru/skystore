from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()[:5]
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/home.html', context)


def product_card(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    context = {
        'object': product_item
    }
    return render(request, 'catalog/card.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('contact_form.txt', 'w+') as form_file:
            form_file.write(f'{name};{phone};{message}')
    return render(request, 'catalog/contacts.html')
