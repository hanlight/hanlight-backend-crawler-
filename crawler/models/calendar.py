"""학사일정"""
from django.db import models


class CalenderModel(models.Model):
    class Meta:
        db_table = "CalenderModel"
        verbose_name = 'CalenderModel'
        verbose_name_plural = 'CalenderModel'

    year = models.IntegerField()
    month = models.IntegerField()
    date = models.IntegerField()
    detail = models.CharField(max_length=100)

    def __str__(self):
        return '%d - %d - %d' % (self.year, self.month, self.date)
