import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

SITES_MAPPING = [
  # {
  #   'url': "https://www.theonion.com/",
  #   'div_selector': 'article',
  #   'div_class': 'js_post_item'
  # },
  {
    'url': 'https://www.bbc.com/',
    'div_selector': 'div',
    'div_class': 'media',
  }
]

def get_news(session, url, div_selector, div_class):
  content = session.get(url, verify=False).content
  soup = BSoup(content, "html.parser")
  return soup.find_all(div_selector, {"class": div_class})

def save_news(source_url, news):
  for article in news:
    print("======", article)
    title = article.find_all('a', {"class": 'media__link'})
    print("TITLE: ", title)
    if len(title) > 0:
      title = title[0].contents[0]
    else:
      title = "NO TITLE"
    image_src = article.find('img')['src']
    print("IMAGE: ", image_src)
    href = source_url[:-1] + article.find('a')['href']
    print("HREF: ", href)

    fields = {
      'title': title,
      'url': href,
      'image': image_src
    }

    # Do not save duplicates
    new_headline = Headline.objects.get_or_create(**fields)

def scrape(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}

  for source in SITES_MAPPING:
    news = get_news(session, source['url'], source['div_selector'], source['div_class'])
    print("SCRAPE: ", source['url'])
    print("NEWS: ", len(news))
    save_news(source['url'], news)
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