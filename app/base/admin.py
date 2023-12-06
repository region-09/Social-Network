from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Message)
admin.site.register(models.Friend)
admin.site.register(models.Media)
admin.site.register(models.Like)
admin.site.register(models.Comment)
admin.site.register(models.Shared)
admin.site.register(models.Requests)
admin.site.register(models.ProfileInfo)