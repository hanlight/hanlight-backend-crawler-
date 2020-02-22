"""급식"""
from django.db import models

class MealModel(models.Model):
    month = models.IntegerField(default=0)
    date = models.IntegerField(default=0)
    detail = models.CharField(max_length=150, null = True)

    def __str__(self):
        return '%d - %d' % (self.month, self.date)
