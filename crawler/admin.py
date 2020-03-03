from django.contrib import admin
from crawler.models.calendar import CalenderModel
from crawler.models.meal import MealModel


admin.site.register(MealModel)
admin.site.register(CalenderModel)
