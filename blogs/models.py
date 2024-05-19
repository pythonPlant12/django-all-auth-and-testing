from django.db import models


class Blogs(models.Model):
    name_blog = models.CharField(max_length=200)
    pages = models.IntegerField(null=True)
    author = models.ForeignKey('authors.Authors', on_delete=models.CASCADE)