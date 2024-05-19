from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    is_active = models.BooleanField()
