from django.urls import path
from django.conf.urls import url
from news import views
#from news.views import scrape, news_list, delete_all


urlpatterns = [
  
  #django rest framework patterns
  url(r'^api/roundups/$',
    views.RoundupList.as_view(),
    name=views.RoundupList.name),
  url(r'api/roundups/(?P<pk>[0-9])/$',
    views.RoundupDetail.as_view(),
    name=views.RoundupDetail.name),
  url(r'^api/introductions/$',
    views.IntroductionList.as_view(),
    name=views.IntroductionList.name),
  url(r'api/introductions/(?P<pk>[0-9])/$',
    views.IntroductionDetail.as_view(),
    name=views.IntroductionDetail.name),
  url(r'^api/categories/$',
    views.CategoryList.as_view(),
    name=views.CategoryList.name),
  url(r'api/categories/(?P<pk>[0-9])/$',
    views.CategoryDetail.as_view(),
    name=views.CategoryDetail.name),
  url(r'^api/sections/$',
    views.SectionList.as_view(),
    name=views.SectionList.name),
  url(r'api/sections/(?P<pk>[0-9])/$',
    views.SectionDetail.as_view(),
    name=views.SectionDetail.name),
  url(r'^api/publications/$',
    views.PublicationList.as_view(),
    name=views.PublicationList.name),
  url(r'api/publications/(?P<pk>[0-9])/$',
    views.PublicationDetail.as_view(),
    name=views.PublicationDetail.name),
  url(r'^api/headlines/$',
    views.HeadlineList.as_view(),
    name=views.HeadlineList.name),
  #headlinedetail
  url(r'api/headlines/(?P<pk>[0-9])/$',
    views.HeadlineDetail.as_view(),
    name=views.HeadlineDetail.name),
  url(r'^api/$',
    views.ApiRoot.as_view(),
    name=views.ApiRoot.name),
  #news app url patterns
  path('scrape/', views.scrape, name="scrape"),
  path('delete/', views.delete_all, name="delete"),
  path('', views.news_list, name="home"),
  path(r'export_headlines/',
    views.export_headlines,
    name='export_headlines'),
]