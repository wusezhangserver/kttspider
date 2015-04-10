from  selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
import  time
import  uuid

def crawMorningDailyNews(link):
    listArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainContext = browsor.find_element_by_id('listArticle')
    listContext = mainContext.find_elements_by_class_name('boxa')
    initImage = CommonsInitValue.initTempImage()
    for context in listContext:
        try:
            imageContext = context.find_element_by_class_name('pic')
            imageUrl = imageContext.find_element_by_tag_name('img').get_attribute('src')
        except NoSuchElementException,e:
            imageUrl = initImage
        title = context.find_element_by_tag_name('h4').text
        linkUrl = context.find_element_by_tag_name('h4')\
                          .find_element_by_tag_name('a').get_attribute('href')
        descriptContext = context.find_element_by_tag_name('p').text
        pubDate = time.strftime("%Y-%m-%d %X",time.localtime())
        listArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'STOCK','CXNET'])
    return listArray

def writeMorningDailyNews():
    link = 'http://finance.caixin.com/'
    listArray = crawMorningDailyNews(link)
    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'CXNET'  AND  NEWSFLAG='STOCK' "
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = ' INSERT MORNING_FINANCENEWS_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,listArray)
