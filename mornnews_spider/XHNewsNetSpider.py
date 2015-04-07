from  selenium import webdriver
import sys
sys.path.append("../commonutils_spider/")
import time
import uuid


def  crawXHNewsNetDataSource(link):
     currentArray = []
     browsor = webdriver.PhantomJS()
     browsor.get(link)
     mainContext = browsor.find_element_by_id('tabCon')
     mainDiv = mainContext.find_element_by_id('showData0')
     listDiv = mainDiv.find_elements_by_class_name('clearfix')
     print listDiv
     for div in listDiv:
         #title = div.find_element_by_tag_name('h3').text
         descriptContext = div.find_element_by_class_name('summary').text
         print  descriptContext
         createDate = div.find_element_by_class_name('time').text
         pubDate = time.strftime("%Y-%m-%d",time.localtime())
         print createDate
         if createDate == pubDate:
            print '---'
            #currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'CHINA','XHNET'])
     return currentArray


def writeXHNewsNetDataSource():
    link = 'http://www.news.cn/finance/'

    #dbManager = CommonsMysqlUtils._dbManager
    SQL = " DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'XHNET' " \
          " AND  NEWSFLAG='CHINA' "
    #dbManager.executeUpdateOrDelete(SQL)

    currentArray = crawXHNewsNetDataSource(link)
    formatSQL =  'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    #dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    writeXHNewsNetDataSource()