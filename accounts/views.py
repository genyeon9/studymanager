from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    else:
        return redirect('study:mystudy')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)

    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })


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
    current_user = request.user
    profile_info = current_user.profile
    return render(request, 'accounts/profile.html', {'profile_info': profile_info})
