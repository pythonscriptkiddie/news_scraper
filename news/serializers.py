from rest_framework import serializers
from news.models import Headline
from news.models import Publication

class PublicationSerializer(serializers.ModelSerializer):

    headlines = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='headline-detail')

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
                    'image',
                    'article_url',
                    'publication',
                    'url',)