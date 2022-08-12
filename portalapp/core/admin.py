from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from core import models

admin.site.register(models.SupportedLanguage)
admin.site.register(models.ApplicationSetting)

