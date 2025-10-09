from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib import messages

from config.settings import EMAIL_HOST_USER
from .forms import UserRegistrationForm, UserProfileEditForm
from .models import CustomUser


class RegisterView(CreateView):
    """Контроллер для регистрации"""
    form_class = UserRegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """Переопределение метода валидации формы для отправки приветственного письма после регистрации"""
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        """Метод отправки приветственного письма после регистрации"""
        subject = "Добро пожаловать в наш интернет магазин"
        message = "Спасибо, что зарегистрировались в нашем магазине!"
        recipient_list = [user_email]
        send_mail(subject, message, EMAIL_HOST_USER, recipient_list)


class UserProfileEditView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования профиля"""
    model = CustomUser
    form_class = UserProfileEditForm
    template_name = "profile_edit.html"
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        """Метод получения информации о пользователе"""
        return self.request.user

    def form_valid(self, form):
        """Метод для отправки сообщения об успешном обновлении"""
        messages.success(self.request, "Ваш профиль был успешно обновлен!")
        return super().form_valid(form)

    def form_invalid(self, form):
        """Метод для отправки сообщения об ошибках формы"""
        messages.error(self.request, "Пожалуйста, исправьте ошибки в форме.")
        return super().form_invalid(form)
