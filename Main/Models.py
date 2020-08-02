from __future__ import unicode_literals
from django.db import models


class Main(models.Model):

    Name = models.CharField(max_length=50)
    About = models.TextField(default='-')

    fb = models.CharField(max_length=50)
    tw = models.CharField(max_length=50)
    yut = models.CharField(max_length=50)
    Telephone = models.CharField(max_length=50)
    link = models.CharField(max_length=50)


    set_name = models.CharField(max_length=50)



    def __str__(self):
       return self.set_name + str(self.pk)
    





        
