from django.contrib.auth.forms import UserCreationForm
from django import forms

from catalog.forms import StyleFormMixin
from users.models import CustomUser


class UserRegistrationForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")


class UserProfileEditForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = CustomUser

        fields = (
            "avatar",
            "phone",
            "country",
        )
