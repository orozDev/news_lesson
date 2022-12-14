from django.urls import path
from .views import ListNewsApiView, DetailNewApiView

urlpatterns = [
    path('news/', ListNewsApiView.as_view()),
    path('news/<int:pk>/', DetailNewApiView.as_view()),
]
