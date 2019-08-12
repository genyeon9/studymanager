from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm, LoginForm, UserEditForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView


# Create your views here.
class UserCreateView(CreateView):
    template_name = 'accounts/signup_form.html'
    form_class = SignupForm
    success_url = reverse_lazy('accounts:login')


class Login(LoginView):
    providers = []
    for provider in get_providers():
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    template_name = 'accounts/login_form.html'
    extra_context = {'providers': providers}


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def profile_revise(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            us = form.save()
            return redirect("accounts:profile")
    else:
        profileform = UserEditForm(instance=request.user)
        forms = {'profileform': profileform}
        return render(request, 'accounts/profile_revise.html', forms)