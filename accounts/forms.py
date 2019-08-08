from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Profile, StudyUser


class SignupForm(UserCreationForm):
    nickname = forms.CharField()
    phone_number = forms.CharField()
    address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = StudyUser
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()
        Profile.objects.create(
            user=user,
            phone_number=self.cleaned_data['phone_number'],
            address=self.cleaned_data['address'],
            nickname=self.cleaned_data['nickname'],
        )
        return user
        # user = StudyUser(**self.cleaned_data)
        # return user


class LoginForm(AuthenticationForm):
    class Meta:
        model = StudyUser


