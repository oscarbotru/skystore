from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import EmailField

from catalog.forms import StyleFormMixin
from users.models import User


class LoginForm(StyleFormMixin, AuthenticationForm):
    pass


class RegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)
        field_classes = {"email": EmailField}
