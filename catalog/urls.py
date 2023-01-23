from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
]
