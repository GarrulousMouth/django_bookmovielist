from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Chapter(models.Model):
    name = models.CharField(max_length=250, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural = 'Chapters'

class BookMovieList(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'BookMovieList'
        verbose_name_plural = 'BookMovieLists'

class ListItem(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    year_of_issue = models.DateField(max_length=4, null=True, blank=True)
    day_complete = models.DateField(null=True, blank=True)
    likes = models.BooleanField(default=False)
    bookmovieid = models.ForeignKey(BookMovieList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ListItem'
        verbose_name_plural = 'ListItems'