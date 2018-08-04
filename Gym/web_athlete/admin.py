from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.fields)
admin.site.register(models.member)
admin.site.register(models.class_times)