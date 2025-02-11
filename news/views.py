import csv
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
import newspaper
from news.models import Headline
from news.models import Publication
from news.models import Section
from news.models import Category
from news.models import Roundup
from news.models import Introduction
from news.serializers import HeadlineSerializer
from news.serializers import PublicationSerializer
from news.serializers import SectionSerializer
from news.serializers import CategorySerializer
from news.serializers import IntroductionSerializer
from news.serializers import RoundupSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import HttpResponse

class IntroductionList(generics.ListCreateAPIView):
  queryset = Introduction.objects.all()
  serializer_class = IntroductionSerializer
  name = 'introduction-list'

class IntroductionDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Introduction.objects.all()
  serializer_class = IntroductionSerializer
  name = 'introduction-detail'

class RoundupList(generics.ListCreateAPIView):
  queryset = Roundup.objects.all()
  serializer_class = RoundupSerializer
  name = 'roundup-list'

class RoundupDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Roundup.objects.all()
  serializer_class = RoundupSerializer
  name = 'roundup-detail'

class HeadlineList(generics.ListCreateAPIView):
  queryset = Headline.objects.all()
  serializer_class = HeadlineSerializer
  name = 'headline-list'

class HeadlineDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Headline.objects.all()
  serializer_class = HeadlineSerializer
  name = 'headline-detail'

class PublicationList(generics.ListCreateAPIView):
  queryset = Publication.objects.all()
  serializer_class = PublicationSerializer
  name = 'publication-list'

class PublicationDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Publication.objects.all()
  serializer_class = PublicationSerializer
  name = 'publication-detail'

class SectionList(generics.ListCreateAPIView):
  queryset = Section.objects.all()
  serializer_class = SectionSerializer
  name = 'section-list'

class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Section.objects.all()
  serializer_class = SectionSerializer
  name = 'section-detail'

class CategoryList(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  name = 'category-list'

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  name = 'category-detail'

class ApiRoot(generics.GenericAPIView):
  name='api-root'
  def get(self, request, *args, **kwargs):
    return Response({
      'roundups': reverse(RoundupList.name, request=request),
      'introductions': reverse(IntroductionList.name, request=request),
      'categories': reverse(CategoryList.name, request=request),
      'sections': reverse(SectionList.name, request=request),
      'headlines': reverse(HeadlineList.name, request=request),
      'publications': reverse(PublicationList.name, request=request)
    })

##### non api related code

#SITES_MAPPING = [
  # {
  #   'url': "https://www.theonion.com/",
  #   'div_selector': 'article',
  #   'div_class': 'js_post_item'
  # },
#  {
#    'url': 'https://www.bbc.com/',
#    'div_selector': 'div',
#    'div_class': 'media',
#  }
#]

#SITES = [
#  'https://www.somaliaffairs.com',
#  'https://sudantribune.com',
#  'https://nation.africa/kenya',
#  'https://www.business-standard.com',
#  'https://www.vanguardngr.com',
#]



# def get_news(session, url, div_selector, div_class):
#   content = session.get(url, verify=False).content
#   soup = BSoup(content, "html.parser")
#   return soup.find_all(div_selector, {"class": div_class})

# def save_news(source_url, news):
#   for article in news:
#     print("======", article)
#     title = article.find_all('a', {"class": 'media__link'})
#     print("TITLE: ", title)
#     if len(title) > 0:
#       title = title[0].contents[0]
#     else:
#       title = "NO TITLE"
#     image_src = article.find('img')['src']
#     print("IMAGE: ", image_src)
#     href = source_url[:-1] + article.find('a')['href']
#     print("HREF: ", href)

#     fields = {
#       'title': title,
#       'url': href,
#       'image': image_src
#     }

#     # Do not save duplicates
#     new_headline = Headline.objects.get_or_create(**fields)

SITES = [i for i in Publication.objects.all()]
#comment out the above list comprehension before modifying the 
#Publication object

def save_article(article, publication_id=None):
  print("title: ", article.title)
  print("headline_url: ", article.url)
  print("text: ", article.text)
  print("keywords: ", article.keywords)
  print('publication_id', publication_id or None)
  # article_title = article.title.replace('\n', '').strip()
  fields = {
    'title': article.title.replace('\n', '').strip() if article.title else 'No title',
    'article_url': article.url,
    'image': article.top_image,
    'publication': Publication.objects.get(id=publication_id)
  }
  # print("======", fields)
  # Do not save duplicates
  new_headline = Headline.objects.get_or_create(**fields)

#def save_publication(article):
#  print("url: ")

def scrape(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}

  # for source in SITES_MAPPING:
  #   news = get_news(session, source['url'], source['div_selector'], source['div_class'])
  #   print("SCRAPE: ", source['url'])
  #   print("NEWS: ", len(news))
  #   save_news(source['url'], news)

  for source in SITES:
    publication_id = source.id
    print("SITE: ", source.homepage_url)
    paper_build = newspaper.build(source.homepage_url)
    print(len(paper_build.articles))
    for article in paper_build.articles:
      save_article(article, publication_id)
  return redirect("../")

def delete_all(request):
  print("DELETE ALL")
  Headline.objects.all().delete()
  return redirect("../")

def news_list(request):
  headlines = Headline.objects.all()
  context = {
      'object_list': headlines,
  }
  return render(request, "news/home.html", context)

def export_headlines(request):
    # Create the HttpResponse object with the appropriate CSV header.
    headlines = Headline.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export_headlines.csv"'

    writer = csv.writer(response)
    writer.writerow(['url', 'title'])
    for headline in headlines:
      writer.writerow([headline.article_url, headline.title])
    
    #writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response