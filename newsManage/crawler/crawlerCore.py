# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import os
import urllib2
import django
import json
import traceback
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newsSystem.settings")
django.setup()
from newsManage.models import NewsInfo

# 导入所需要的模块
class newsCrawler():
    def url(self, url):
        html = self.request(url)  ##
        soup = BeautifulSoup(html.text, 'lxml',from_encoding="utf-8")
        return soup

    def request(self, url):  ##这个函数获取网页的response 然后返回
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'referer':   "http://news.qq.com/articleList/rolls/"# 伪造一个访问来源
        }
        content = requests.get(url, headers=headers)
        return content

    def parseArticle(self,jsonObj):
        try:
            title = jsonObj['title']
            newstype = jsonObj['newstype']
            time = jsonObj['time']
            url = jsonObj['docurl']
            label = jsonObj['label']
            imgurl = jsonObj['imgurl']
            pk = url.split('/')[-1].split('.')[0]
            print title,newstype,time,url,pk,imgurl
            Articlesoup = self.url(url)
            article_wy_ = Articlesoup.find_all('div', class_='post_text')[0]
            if imgurl:
                pwd = os.getcwd()
                picture = urllib2.urlopen(imgurl).read()
                root = os.path.split(pwd)[0]
                webPath = 'static\\viewPicture\\%s.%s' % (pk, 'jpg')
                filePath = os.path.join(root, webPath)
                webPath = '/'+webPath.replace('\\','/')
                fo = open(filePath, 'wb')
                fo.write(picture)
                fo.flush()
                fo.close()
            final_article = article_wy_.prettify()
            newsInfo = NewsInfo(newstype,title,time,webPath,label,final_article,pk)
            newsInfo.save()
        except Exception, e:
            print traceback.print_exc(),str(e)
            print '新闻爬取错误1条，跳过'
            return
# 设置启动函数
def main():

    listUrl = ['http://sports.163.com/special/000587PR/newsdata_n_nba.js?callback=data_callback',
               'http://sports.163.com/special/000587PR/newsdata_n_china.js?callback=data_callback',
               'http://sports.163.com/special/000587PR/newsdata_n_cba.js?callback=data_callback',
               'http://sports.163.com/special/000587PR/newsdata_n_world.js?callback=data_callback',
               'http://sports.163.com/special/000587PR/newsdata_n_allsports.js?callback=data_callback']
    nc = newsCrawler()
    for url in listUrl[:1]:
        soup = nc.url(url)
        strResult = soup.find_all('p')[0].get_text()
        # 去除头尾
        strJson = strResult[14:-1]
        print strJson
        objJson = json.loads(strJson)
        for _ in objJson:
            nc.parseArticle(_)

    # strResult = soup.find_all('div',attrs={"class":"newsdata_wrap"})[0]
    # print '主框架：',strResult
    # currentList = strResult.find_all('li',attrs={"class":"newsdata_item current"})
    # print currentList
main()