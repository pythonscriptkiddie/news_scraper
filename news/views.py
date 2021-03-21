import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
import newspaper
from news.models import Headline
from news.models import Publication
from news.serializers import HeadlineSerializer
from news.serializers import PublicationSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

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

class ApiRoot(generics.GenericAPIView):
  name='api-root'
  def get(self, request, *args, **kwargs):
    return Response({
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