from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, *args, **kwargs):
        name = self.request.POST.get('name')
        phone = self.request.POST.get('phone')
        message = self.request.POST.get('message')
        with open('contact_form.txt', 'w+') as form_file:
            form_file.write(f'{name};{phone};{message}')
        return redirect(reverse('catalog:contacts'))


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
