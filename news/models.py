from django.db import models

class Section(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name


class Publication(models.Model):
  title = models.CharField(max_length=200)
  homepage_url = models.URLField(unique=True)

  def __str__(self):
    return self.homepage_url

  class Meta:
    ordering = ('homepage_url',)

class Headline(models.Model):
  title = models.CharField(max_length=200)
  # source = models.CharField(max_length=200)
  image = models.URLField(null=True, blank=True)
  article_url = models.TextField()
  publication = models.ForeignKey(
    Publication,
    related_name='headlines',
    on_delete=models.SET_NULL,
    blank=True,
    null=True
  )
  #category = models.ForeignKey(
  #  Category,
  #  related_name='headlines',
 #   on_delete=models.SET_NULL,
 #   blank=True,
 #   null=True
 # )

  def __str__(self):
    return self.title
  
  class Meta:
    ordering = ('title',)
