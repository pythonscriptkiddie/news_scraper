# news_scraper

A Django app to scrape through the news and analyze them using AI.

Spiders should crawl on the news websites and extract article info.

Each article should have:
* Url
* Text (first paragraph?)
* Tags
* Author
* Date

The user should be able to filter on:
* News source
* Tag
* Author
* Date

Use cases:
* Find article from specific source/author
* Apply sentiment analysis on article texts
* Create wordcloud per day with the tags

TODOs:
* PSQL database
* Create tables and connect them
** Article
** Author -> Article
** Soure -> Article
* Angular front end
* Create filter

News Scraper based on https://data-flair.training/blogs/django-project-news-aggregator-app/

Deployed to :
https://news-scrapr-ai.herokuapp.com/
