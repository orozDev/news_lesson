from report.models import News
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def is_owner(func):

    def inner(request, id, *args, **kwargs):
        news = News.objects.get(id=id)
        if request.user == news.author:
            return func(request, id, *args, **kwargs)
        return redirect('/')

    return inner


def is_not_authenticated(func):
    
    def inner(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect('/')
    return inner
    
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')

    user = User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
    )
    user.set_password(password)
    user.save()
    return user


def increase_views(func):
    
    def inner(request, id, *args, **kwargs):
        news = News.objects.get(id=id)
        if news.author != request.user:
            news.views += 1
            news.save()
        return func(request, id, *args, **kwargs)
    
    return inner