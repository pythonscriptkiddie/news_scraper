import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

SITES_MAPPING = [
  {
    'url': "https://www.theonion.com/",
    'div_selector': 'article',
    'div_class': 'js_post_item'
  }
]

def get_news(session, url, div_selector, div_class):
  content = session.get(url, verify=False).content
  soup = BSoup(content, "html.parser")
  return soup.find_all(div_selector, {"class": div_class})

def save_news(news):
  for article in news:
    main = article.find_all('a')[0]
    link = main['href']
    image_src = '' # str(main.find('img')['srcset']).split(" ")[-4]
    title = 'test' # main['title']

    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.image = image_src
    new_headline.save()

def scrape(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}

  for source in SITES_MAPPING:
    news = get_news(session, source['url'], source['div_selector'], source['div_class'])
    print("SCRAPE: ", source['url'])
    print("NEWS: ", len(news))
    save_news(news)
  return redirect("../")

def delete_all(request):
  print("DELETE ALL")
  Headline.objects.all().delete()
  return redirect("../")

def news_list(request):
  headlines = Headline.objects.all()[::-1]
  context = {
      'object_list': headlines,
  }
  return render(request, "news/home.html", context)