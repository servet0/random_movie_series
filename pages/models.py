from django.db import models

class NumberMovie(models.Model):
    numbermovie = models.CharField(max_length=20)

    
class NumberSeries(models.Model):
    numberseries = models.CharField(max_length=20)


# Create your models here.
