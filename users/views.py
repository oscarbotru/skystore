from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic

from users.forms import LoginForm, RegisterForm


class SigninView(LoginView):
    template_name = 'users/authorization.html'
    success_url = reverse_lazy('users:dashboard')
    form_class = LoginForm


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')


class ResetView(generic.TemplateView):
    pass


class ConfirmView(generic.TemplateView):
    pass


class SignOutView(LogoutView):
    pass


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'users/index.html'
