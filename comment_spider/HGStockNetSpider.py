from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
import uuid

def crawDailyStockComments(link):
    currentList = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainlist =browsor.find_element_by_class_name('ul-news-list').find_elements_by_tag_name('li')
    for context in mainlist:
        linkUrl = context.find_element_by_tag_name('a').get_attribute('href')
        title = context.text
        pubDate = CommonsInitValue.initNowTime()
        currentList.append([str(uuid.uuid1()),linkUrl,title,pubDate,'[...]','STOCK','HGNET'])
    return currentList

def writeDailyStockComments():
    link = 'http://stock.huagu.com/hgsd/'
    currentArray = crawDailyStockComments(link)

    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  COMMENTS_STOCK_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'HGNET'"
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = ' INSERT COMMENTS_STOCK_RESOURCE_TABLE ' \
                ' (KEYID,LINKURL,TITLE,PUBDATE,DESCRIPTCONTEXT,COMMENTFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)