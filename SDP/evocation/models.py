
from django.db import models
# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=122)
    email = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)

    def str(self):
        return self.username


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

        class Meta:
             verbose_name_plural = 'cities'