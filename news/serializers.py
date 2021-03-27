from rest_framework import serializers
from news.models import Headline
from news.models import Publication
from news.models import Section
from news.models import Category
from news.models import Roundup
from news.models import Introduction

class IntroductionSerializer(serializers.HyperlinkedModelSerializer):
    roundups = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='roundup-detail',
    )

    class Meta:
        model = Introduction
        fields = ('id',
                'text')

class RoundupSerializer(serializers.HyperlinkedModelSerializer):

    introduction = serializers.SlugRelatedField(
        queryset=Roundup.objects.all(),
        slug_field='title'
    )

    class Meta:
        model = Roundup
        fields = ('id',
                'title',
                'introduction',
                'start_date',
                'end_date')

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    headlines = serializers.SlugRelatedField(
        queryset=Headline.objects.all(),
        many=True,
        slug_field='title'
    )

    section = serializers.SlugRelatedField(
        queryset=Section.objects.all(),
        slug_field='name')

    class Meta:
        model = Category
        fields = ('id',
                'name',
                'url',
                'section',
                'headlines')

class SectionSerializer(serializers.HyperlinkedModelSerializer):

    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        many=True,
        slug_field='name'
    )

    class Meta:
        model = Section 
        fields = ('id',
                'name',
                'section_type',
                'url',
                'categories')

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

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Headline

        fields = ('id',
                'title',
                'article_url',
                'publication',
                'category')
                #'url')