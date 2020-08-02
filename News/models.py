from __future__ import unicode_literals
from django.db import models


class News(models.Model):

    Name = models.CharField(max_length=50)
    title_of_news = models.TextField()
    body_of_news = models.TextField()
    news_image = models.ImageField(
            null=True,
            blank=True)
    timestamp = models.DateTimeField()
    author = models.CharField(max_length=50)
    cat_name = models.CharField(default="newspaper",max_length=50)
    news_view = models.IntegerField(default=0)
    cat_id = models.IntegerField(default=0)



    def __str__(self):
       return self.title_of_news + str(self.pk)
    
