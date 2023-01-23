from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
]
