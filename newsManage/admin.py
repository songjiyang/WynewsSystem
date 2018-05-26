# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from .models import NewsInfo


admin.site.site_header = '新闻信息管理系统'
admin.site.site_title = '天下新闻'

class NewInfoAdmin(admin.ModelAdmin):
    list_display = ('newsDateTime','newsTile')

admin.site.register(NewsInfo,NewInfoAdmin)