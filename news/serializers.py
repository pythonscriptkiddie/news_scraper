from rest_framework import serializers
from news.models import Headline
from news.models import Publication
from news.models import Section

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section 
        fields = ('id',
                'name',
                'url')

class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    headlines = serializers.SlugRelatedField(
        queryset=Headline.objects.all(),
        many=True,
        slug_field='title'
    )

    class Meta:
        model = Publication
    
        fields = ('id',
                'title',
                'homepage_url',
                'headlines')
                #'url')

class HeadlineSerializer(serializers.ModelSerializer):

    publication = serializers.SlugRelatedField(
        queryset=Publication.objects.all(),
        slug_field='title')

    class Meta:
        model = Headline

        fields = ('id',
                'title',
                'article_url',
                'publication',)
                #'url')