from selenium import webdriver
from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
import uuid

def crawFinanceHLDataSource(link):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainlist = browsor.find_element_by_class_name('news_list').find_elements_by_class_name('list')
    for context in mainlist:
        imageUrl = context.find_element_by_tag_name('img').get_attribute('src')
        title = context.find_element_by_class_name('title').text
        linkUrl = context.find_element_by_class_name('title').find_element_by_tag_name('a').get_attribute('href')
        descriptContext = context.find_element_by_tag_name('p').text
        pubDate = CommonsInitValue.initNowTime()
        currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'STOCK','TAKCHINA'])
    return currentArray
     
def writeFinanceHLDataSource():
    link = 'http://finance.takungpao.com/'
    currentArray = crawFinanceHLDataSource(link)

    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE" \
          "  WHERE  SOURCEFLAG = 'TAKCHINA' AND  NEWSFLAG='STOCK'"
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = 'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)