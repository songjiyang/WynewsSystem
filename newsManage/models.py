from django.db import models
# -*- coding: utf-8 -*-
# Create your models here.



class NewsInfo(models.Model):
    newsType = models.CharField(max_length=50)
    newsTile = models.CharField(max_length=200)
    newsDateTime = models.CharField(max_length=50)
    viewPicturePath = models.CharField(max_length=500)
    newsLabel = models.CharField(max_length=200,default=u'其他')
    content = models.TextField()
    priKey = models.CharField(max_length=100, primary_key=True)