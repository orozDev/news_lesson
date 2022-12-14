from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Categories(models.Model):

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    slug = models.SlugField(unique=True, verbose_name='slug название', null=True)
    title = models.CharField(max_length=100, verbose_name='название категотрии')

    def __str__(self):
        return f'{self.title}'


class Tags(models.Model):
    
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    title = models.CharField(max_length=100, verbose_name='название тега')

    def __str__(self):
        return f'{self.title}'


class News(models.Model):

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
    
    title = models.CharField(max_length=300, verbose_name='заголовок')
    image = models.ImageField(verbose_name='изображение', upload_to='images/', null=True)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name='категория')
    tags = models.ManyToManyField('Tags', verbose_name='теги')
    content =  models.TextField(verbose_name='контетн')
    date = models.DateField(verbose_name='дата добавление', auto_now_add=True)
    views = models.PositiveIntegerField(verbose_name='просмотры', default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор', null=True)


    def __str__(self):
        return f'{self.title}'




# Create your models here.