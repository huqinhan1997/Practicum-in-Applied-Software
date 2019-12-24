from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Staff)
admin.site.register(models.Club)
admin.site.register(models.Activity)
admin.site.register(models.Join)
admin.site.register(models.Apply)
admin.site.register(models.News)