import random

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from users.forms import LoginForm, RegisterForm
from users.models import User


class SigninView(LoginView):
    template_name = 'users/authorization.html'
    success_url = reverse_lazy('users:dashboard')
    form_class = LoginForm


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        self.object.verification_key = ''.join([str(random.randint(0, 9)) for _ in range(21)])
        send_mail(
            'Верификация',
            f'Для верификации перейдите по ссылке http://localhost:8000/users/verify/{self.object.verification_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        super().form_valid(form)


class ResetView(generic.TemplateView):
    pass


class ConfirmView(generic.TemplateView):

    def get(self, *args, **kwargs):
        key = self.kwargs.get('key')
        user = User.objects.filter(verification_key=key).first()
        if user:
            user.is_verified = True
            user.verification_key = None
            user.save()
            login(self.request, user)

        return redirect('/')


class SignOutView(LogoutView):
    pass


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'users/index.html'
