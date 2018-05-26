# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import NewsInfo
from django.core.paginator import Paginator
from django.utils.safestring import mark_safe
# Create your views here.
def index(request):
    context = {}
    return render(request, 'newsManage/index.html', context)

def archive(request):
    type = request.GET.get('type')  #1-NBA  2-国际足球  3-国内足球  4-CBA 5-综合
    tmpList = ''
    if type == '1':
        tmpList = NewsInfo.objects.filter(newsLabel=u'NBA')
    elif type == '2':
        tmpList = NewsInfo.objects.filter(newsLabel=u'国际足球')
    elif type == '3':
        tmpList = NewsInfo.objects.filter(newsLabel=u'中国足球')
    elif type == '4':
        tmpList = NewsInfo.objects.filter(newsLabel=u'CBA')
    elif type == '5':
        tmpList = NewsInfo.objects.filter(newsLabel=u'综合')
    else:
        tmpList = NewsInfo.objects.all()
    date = request.GET.get('date')
    if date!=None:
        tmpList = tmpList.filter(newsDateTime__startswith=date)
    newsinfo_list = tmpList.values('newsTile','newsType','newsDateTime','viewPicturePath','priKey')
    p = Paginator(newsinfo_list,8)
    page = request.GET.get('page')
    if page == None:
        page = 1
    pageObj = p.page(page)
    context = {'paginator': p, 'pageObj': pageObj, 'newsinfo_list': pageObj.object_list, 'currentPage': int(page),'date':date,'type':type}
    return render(request, 'newsManage/archive.html', context)


def single(request):
    pk = request.GET.get('pk')
    newsinfo = NewsInfo.objects.get(priKey=pk)
    pageHtml = mark_safe(newsinfo.content)
    context = {'newsinfo':newsinfo,'pageHtml':pageHtml}
    return render(request, 'newsManage/single.html', context)