from rest_framework import serializers
from news.models import Headline
from news.models import Publication

class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    headlines = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='headline-detail'
    )

    class Meta:
        model = Publication
    
        fields = ('id',
                'title',
                'homepage_url',
                'headlines',
                'url')

class HeadlineSerializer(serializers.HyperlinkedModelSerializer):

    publication = serializers.SlugRelatedField(
        queryset=Publication.objects.all(),
        slug_field='title')

    class Meta:
        model = Headline

        fields = ('id',
                'title',
                'article_url',
                'publication',
                'url')