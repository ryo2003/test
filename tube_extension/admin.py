from django.contrib import admin
from . import models



@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    pass


