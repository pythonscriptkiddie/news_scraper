from django.urls import path
from news.views import scrape, news_list, delete_all

urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('delete/', delete_all, name="delete"),
  path('', news_list, name="home"),
]