from django.contrib.auth.forms import UserCreationForm
from django import forms

from catalog.forms import StyleFormMixin
from users.models import CustomUser


class UserRegistrationForm(StyleFormMixin, UserCreationForm):
    """Класс для регистрации и авторизации пользователей"""
    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")


class UserProfileEditForm(StyleFormMixin, forms.ModelForm):
    """Класс для редактирования профиля"""
    class Meta:
        model = CustomUser

        fields = (
            "avatar",
            "phone",
            "country",
        )
