from report.models import News, Categories, Tags
from rest_framework import serializers


class CategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields = '__all__'
        
        
class TagsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tags
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    
    category = CategoriesSerializer(many=False)
    tags = TagsSerializer(many=True)
    
    class Meta:
        model = News
        fields = '__all__'
        
