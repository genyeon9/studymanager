from random import randint

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import StudyUser

from accounts.forms import SignupForm, LoginForm

from .forms import GroupForm, RegisterForm
from .models import Group, Membership
from django import forms

# Create your views here.


def group_list(request):
    gr = Group.objects.all()
    return render(request, 'study/group_list.html', {'group_list': gr, })


def group_detail(request, id):
    group = get_object_or_404(Group, id=id)
    members = Membership.objects.filter(group=group)

    return render(request, 'study/group_detail.html', {
        'group': group, 'members': members,
    })



def group_new(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            while True:
                try:
                    group.invitation_url = str(randint(1, 999999)).zfill(6)
                    group.save()
                    break
                except:
                    pass
            group.save()
            m = Membership.objects.create(person=request.user, group=group)
        return redirect(group)
    else:
        form = GroupForm()
    return render(request, 'study/group_form.html', {
        'form': form,
    })




def group_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = request.user
            group = Group.objects.get(group_name=request.POST['group_name'])
            m = Membership.objects.create(person=user, group=group)
        return redirect(group)
    else:
        form = RegisterForm()
    return render(request, 'study/group_register.html', {
        'form': form,
    })

def group_registerbyurl(request, invitation_url):
    if request.method == 'POST':
        try:
            user = request.user
            group = Group.objects.get(invitation_url=invitation_url)
            membership = [x.person for x in Membership.objects.filter(group=group)]
            if user not in membership:
                m = Membership.objects.create(person=user, group=group)
                return redirect(group)
            else:
                return HttpResponse("중복가입입니다.")

        except:
            form = LoginForm(request.POST)
            id = request.POST['username']
            pw = request.POST['password']
            u = authenticate(username=id, password=pw)

            if u:
                login(request, user=u)
                return render(request, 'study/group_registerbyurl.html', {'group': group,
                                                                          'form': form})


            else:
                return render(request, 'study/group_registerbyurl.html', {'group': group,
                                                                          'form': form,
                                                                          'error':'아이디나 비밀번호가 일치하지 않습니다.'})

                # return render(request, 'study/group_registerbyurl.html', {'group':group})

    else :
        group = Group.objects.get(invitation_url=invitation_url)
        form = LoginForm()
        return render(request, 'study/group_registerbyurl.html', {'group':group,
                                                                  'form':form})



def group_mystudy(request):
    return render(request, 'study/group_mystudy.html')

def mystudy_list(request,id):
    user = get_object_or_404(StudyUser,id=id)
    groups = Membership.objects.filter(person=user)

    return render(request, 'study/mystudy_list.html',{
        'user': user, 'groups': groups,
    })