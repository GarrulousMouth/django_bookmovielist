from django.db import models

# Create your models here.
class ListItem(models.Model):
    name = models.CharField(max_length=250, blank=True)
    author = models.CharField(max_length=250)
    description = models.TextField()
    year_of_issue = models.DateField()
    day_complete = models.DateField()
    likes = models.BooleanField(default=False)

class BookMovieList(models.Model):
    name = models.CharField(max_length=250, unique=True)

