from commonutils_spider import  CommonsMysqlUtils
from commonutils_spider import  CommonsInitValue
from  selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import uuid

def crawYiCaiStockDailyNews(link):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    contextArray = browsor.find_elements_by_tag_name('dl')
    for context in contextArray:
        try:
          titleValue = context.find_element_by_tag_name('h1')
          descriptContext = context.find_element_by_tag_name('p').text
          pubDate = time.strftime("%Y-%m-%d %X",time.localtime())
          linkUrl = context.find_element_by_tag_name('a').get_attribute('href')
          try:
              imageObj = context.find_element_by_tag_name('img')
              imageUrl = imageObj.get_attribute('src')
          except NoSuchElementException,e:
              imageUrl = CommonsInitValue.initTempImage()

        except NoSuchElementException,e:
              continue
        title = titleValue.text
        currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'STOCK','YICAINET'])
    return currentArray
    
def writeYiCaiStockDataSource():
    link = 'http://www.yicai.com/markets/'
    currentArray = crawYiCaiStockDailyNews(link)
    dbManager = CommonsMysqlUtils._dbManager
    SQL = " DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE" \
           "  WHERE  SOURCEFLAG = 'YICAINET' AND  NEWSFLAG='STOCK'"
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = 'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG) ' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)