from django.db import models


class Tax(models.Model):
    name = models.CharField('Name', max_length=50)
    percent = models.FloatField()

    def __str__(self):
        return self.name
