from  selenium import webdriver
from commonutils_spider import CommonsMysqlUtils
import time
import uuid


def crawMorningForexDailyNews(link):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    resultList = browsor.find_element_by_id('analysis_ul').find_elements_by_tag_name('li')
    for div in resultList:
        descriptContext  = div.find_element_by_class_name('touzi_font').find_element_by_tag_name('p').text
        imageUrl = div.find_element_by_class_name('new_6_pic').find_element_by_tag_name('img').get_attribute('src')
        linkUrl = div.find_element_by_class_name('new_6_pic').find_element_by_tag_name('a').get_attribute('href')
        pubDate = time.strftime("%Y-%m-%d %X",time.localtime())
        title = div.find_element_by_class_name('touzi_font').find_element_by_tag_name('h1').text
        currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'FOREX','HTNET'])
    return  currentArray


def writeMorningForexDailyNews():
    linkUrl = 'http://news.fx678.com/news/top/index.shtml'
    currentArray = crawMorningForexDailyNews(linkUrl)
    dbManager = CommonsMysqlUtils._dbManager
    SQL = "  DELETE  FROM  MORNING_OTHERNEWS_RESOURCE_TABLE " \
          "  WHERE  SOURCEFLAG = 'HTNET' AND  NEWSFLAG='FOREX' "
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = ' INSERT MORNING_OTHERNEWS_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)



