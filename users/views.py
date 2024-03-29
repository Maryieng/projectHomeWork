import random

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserPasswordRecoveryForm, UserProfileForm
from users.models import User
import string


def generate_random_password():
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        super().form_valid(form)
        email = form.cleaned_data.get('email')
        send_mail(
            'Поздравляем с регистрацией на сайте!',
            'Добро Пожаловать!',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return super().form_valid(form)


class UserPasswordRecoveryView(FormView):
    template_name = 'users/user_recovery_password.html'
    form_class = UserPasswordRecoveryForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = User.objects.filter(email=email).first()
        random_password = generate_random_password()
        user.password = make_password(random_password)
        user.save()
        send_mail(
            'Запрос на восстановление пароля',
            f'Ваш новый пароль: {random_password}',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
