"""급식"""
from django.db import models


class MealModel(models.Model):
    class Meta:
        db_table = 'MealModel'
        verbose_name = 'MealModel'
        verbose_name_plural = 'MealModel'

    month = models.IntegerField(default=0)
    date = models.IntegerField(default=0)
    detail = models.CharField(max_length=150, blank = True)

    def __str__(self):
        return '%d - %d' % (self.month, self.date)
