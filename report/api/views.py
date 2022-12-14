from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import NewsSerializer, CategoriesSerializer, TagsSerializer
from report.models import News, Categories, Tags


class ListNewsApiView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    

class DetailNewApiView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
