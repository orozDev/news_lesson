from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from report.services import (
    is_owner, 
    is_not_authenticated,
    register,
    increase_views,
)
from django.core.paginator import Paginator
from report.models import *

newsImageSystem = FileSystemStorage('media/images/')
AMOUNT_ITEM = 6

def main(request):              
    news = News.objects.all()
    categories = Categories.objects.all()
    pagin = Paginator(news, AMOUNT_ITEM)
    page = request.GET.get('page', 1)
    current_items = pagin.get_page(page)
    return render(request, 'index.html', {
        'news': current_items, 
        'categories': categories
    })


@increase_views
def item_news(request, id):
    news = News.objects.get(id=id)
    categories = Categories.objects.all()
    return render(request, 'item_news.html', {'news': news, 'categories': categories})


def filter_news(request, slug):
    category = Categories.objects.get(slug=slug)
    #news = News.objects.filter(category__slug=slug)
    news = News.objects.filter(category=category)
    categories = Categories.objects.all()
    return render(request, 'filter_news.html',{
        'news': news, 
        'categories': categories, 
        'category': category,
    })


def search_news(request):
    title = request.GET.get('search')
    news  = News.objects.filter(title__icontains=title)
    return render(request, 'search.html',{
        'news': news, 
        'categories': Categories.objects.all(), 
        'title': title
    })



def login_profile(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            messages.error(request, f'Не существует пользователя или неверный паороль')
        return render(request, 'auth/login.html', {})
    return redirect('/')


def logout_profile(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def filter_news_by_tags(request, id):
    tag = Tags.objects.get(id=id)
    news  = News.objects.filter(tags__id=id)
    categories = Categories.objects.all()
    return render(request, 'filter_news_by_tags.html',{
        'news': news, 
        'categories': categories, 
        'tag': tag,
    })    


@login_required(login_url='/login/')
def my_news(request):
    news = News.objects.filter(author=request.user)
    categories = Categories.objects.all()
    return render(request, 'my_news/my_news.html', {'news': news, 'categories': categories})


@login_required(login_url='/login/')
def create_news(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        image = request.FILES['image']
        category = Categories.objects.get(id=request.POST.get('category'))
        content = request.POST.get('content')   
        newsImageSystem.save(image.name, image)
        news = News.objects.create(
            title = title,
            image = image,
            category = category,
            content = content,
            author=request.user
        )
        tags_id = request.POST.getlist('tags')
        for tag_id in tags_id:
            tag = Tags.objects.get(id=tag_id)
            news.tags.add(tag)
        news.save()
        messages.success(request, f'Вы успешно добавели новость "{news.title}"')
        return redirect('/my_news/')

    categories = Categories.objects.all()
    tags = Tags.objects.all()
    return render(request, 'my_news/create_news.html', {'categories': categories, 'tags': tags})


@login_required(login_url='/login/')
@is_owner
def delete_news(request, id):
    news = News.objects.get(id=id)
    news.delete()
    return redirect('/my_news/')


@login_required(login_url='/login/')
@is_owner
def update_news(request, id):
    if request.method == 'POST':
        news = News.objects.get(id=id)
        title = request.POST.get('title')
        image = request.FILES.get('image', None)
        category = Categories.objects.get(id=request.POST.get('category'))
        content = request.POST.get('content') 
        if image is not None: 
            newsImageSystem.save(image.name, image)
            news.image = image
        news.title = title
        news.category = category
        news.content = content
        for tag in news.tags.all():
            news.tags.remove(tag)
        tags_id = request.POST.getlist('tags')
        for tag_id in tags_id:
            tag = Tags.objects.get(id=tag_id)
            news.tags.add(tag)
        news.save()
        messages.success(request, f'Вы успешно отредактировали новость "{news.title}"')
        return redirect('/my_news/')
            
    categories = Categories.objects.all()
    tags = Tags.objects.all()
    news = News.objects.get(id=id)
    return render(request, 'my_news/update_news.html', {
        'categories': categories,
        'tags': tags,
        'news': news,
    })


@is_not_authenticated
def registration(request):
    if request.method == 'POST':
        user = register(request)
        login(request, user)
        return redirect('/my_news/')
    categories = Categories.objects.all()
    return render(request, 'auth/registration.html', {'categories': categories})  

# Create your views here.
