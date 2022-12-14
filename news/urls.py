from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from report.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('news_item/<int:id>/', item_news, name="item_news"),
    path('filter/<str:slug>/', filter_news, name="filter_news"),
    path('filter_by_tags/<int:id>/', filter_news_by_tags, name="filter_news_by_tags"),
    path('search/', search_news, name="search_news"),

    path('my_news/', my_news, name='my_news'),
    path('my_news/create/', create_news, name='create_news'),
    path('my_news/<int:id>/delete/', delete_news, name='delete_news'),
     path('my_news/<int:id>/update/', update_news, name='update_news'),

    path('login/', login_profile, name='login'),
    path('logout/', logout_profile, name='logout'),
    path('registration/', registration, name='registration'),
    
    path('api/', include('report.api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
