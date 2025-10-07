from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView

from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name ='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

]
