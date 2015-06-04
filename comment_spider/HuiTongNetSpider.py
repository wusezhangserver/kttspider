import HuiTongNetSpiderUtils
import time
import uuid

def crawDailyComments(link):
    currentArray = []


    return currentArray
    

def writeDailyComments():
    link = 'http://www.fx678.com/news/forex/scpl.html'
    currentList = crawDailyComments(link)
    SQL = "DELETE  FROM  COMMENTS_NEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'FX678'"
    formatSQL = ' INSERT COMMENTS_NEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,TITLE,PUBDATE,DESCRIPTCONTEXT,COMMENTFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s)'
