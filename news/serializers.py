from rest_framework import serializers
from news.models import Headline
from news.models import Publication

class PublicationSerializer(serializers.ModelSerializer):
    headlines = serializers.SlugRelatedField(
        queryset=Headline.objects.all(),
        many=True,
        slug_field='title')

    class Meta:
        model = Publication
    
        fields = ('id',
                'homepage_url',
                'headlines',)

class HeadlineSerializer(serializers.ModelSerializer):

    publication = serializers.SlugRelatedField(
        queryset=Publication.objects.all(),
        slug_field='homepage_url')

    class Meta:
        model = Headline

        fields = ('id',
                'title',
                'article_url',
                'publication',
                'url')