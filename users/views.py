from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from .forms import UserRegistrationForm

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш интернет магазин'
        message = 'Спасибо, что зарегистрировались в нашем магазине!'
        recipient_list = [user_email]
        send_mail(subject, message, EMAIL_HOST_USER, recipient_list)
