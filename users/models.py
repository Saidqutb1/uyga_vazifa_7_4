from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250, blank=True, null=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=250)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name

