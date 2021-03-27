from django.db import models

class Introduction(models.Model):
  text = models.TextField(default='', null=True, blank=True)

  def __str__(self):
    return self.text

  class Meta:
    ordering = ('text',)

class Roundup(models.Model):
  title = models.CharField(max_length=200)
  start_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)
  introduction = models.ForeignKey(
    Introduction,
    related_name='roundups',
    on_delete=models.SET_NULL,
    blank=True,
    null=True
  )

  def __str__(self):
    return self.title
  
  class Meta:
    ordering = ('title',)

class Section(models.Model):
  COUNTRY = 'C'
  THEMATIC = 'T'
  TYPE_CHOICES = (
    (COUNTRY, 'Country'),
    (THEMATIC, 'Thematic'),
  )
  name = models.CharField(max_length=200)
  section_type = models.CharField(
    max_length=2,
    choices=TYPE_CHOICES,
    default=COUNTRY
  )

  def __str__(self):
    return self.name

  class Meta:
    ordering = ('name',)

class Category(models.Model):
  name = models.CharField(max_length=200)
  section = models.ForeignKey(
    Section,
    related_name='categories',
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return self.name

  class Meta:
    ordering = ('name',)

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
  category = models.ForeignKey(
    Category,
    related_name='headlines',
    on_delete=models.SET_NULL,
    blank=True,
    null=True
  )

  def __str__(self):
    return self.title
  
  class Meta:
    ordering = ('title',)
