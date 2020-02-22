from django.contrib import admin
from crawler.models.meal import MealModel
from crawler.models.calendar import CalenderModel
# Register your models here.
admin.site.register(MealModel)
admin.site.register(CalenderModel)
