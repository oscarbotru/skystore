from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        VersionFormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = VersionFormSet(self.request.POST, instance=self.object)
        else:
            formset = VersionFormSet(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()

        return super().form_valid(form)
