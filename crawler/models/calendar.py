"""학사일정"""
from django.db import models

class CalenderModel(models.Model):
    year = models.IntegerField(null=False)
    month = models.IntegerField(null=False)
    date = models.IntegerField(null=False)
    detail = models.CharField(max_length=100, null=False)

    def __str__(self):
        return '%d - %d - %d' % (self.year, self.month, self.date)
