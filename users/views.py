from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import User


class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def form_invalid(self, form):
        if not form.user_cache or not form.user_cache.is_active:
            messages.error(self.request, 'Ваш аккаунт не активен!')
            return redirect(reverse_lazy('users:ban'))

        return super().form_invalid(form)


class BanView(TemplateView):
    model = User
    template_name = 'users/ban.html'


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
