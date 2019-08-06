from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name']

class RegisterForm(forms.Form):
    CHOICES = []

    for i in range(Group.objects.count()):
        group_name = Group.objects.get(pk=i+1)
        CHOICES.append(('i', group_name.group_name))

    user_name = forms.CharField()
    group_name = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
