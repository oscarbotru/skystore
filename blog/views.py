from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView

from blog.models import Article


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        object_item = super().get_object(queryset)
        object_item.views += 1
        object_item.save()
        if object_item.views == 100:
            send_mail(
                subject='Обновление по блогу',
                message=f'Статья {object_item.title} достигла 100 просмотров',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['me@mydomain.com']
            )
        return object_item
