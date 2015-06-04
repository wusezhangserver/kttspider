from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
import uuid

def crawCNStockNetDailyNews(link):
    currentList = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainlist = browsor.find_elements_by_class_name('art-list')
    for context in mainlist:
        linkUrl = context.find_element_by_tag_name('a').get_attribute('href')
        title = context.find_element_by_tag_name('a').text
        descriptContext = context.find_element_by_class_name('pic-details').text
        pubDate = CommonsInitValue.initNowTime()
        imageUrl = CommonsInitValue.initTempImage()
        currentList.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'CHINA','21CNNET'])
    return currentList

def writeCNStockNetDailyNews():
    link = 'http://finance.21cn.com/webfocus/internet/'
    currentArray = crawCNStockNetDailyNews(link)

    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = '21CNNET' AND  NEWSFLAG='CHINA'"
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = 'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)