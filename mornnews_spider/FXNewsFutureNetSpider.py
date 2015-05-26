from  selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from commonutils_spider import CommonsMysqlUtils
import uuid

def crawMorningFutureDailyNews(linkUrl):
    currentList = []
    browsor = webdriver.PhantomJS()
    browsor.get(linkUrl)
    contextList = browsor.find_element_by_class_name('yjl_fx168_news_listBox').find_elements_by_tag_name('li')
    for mainContext in contextList:
        pubDate = mainContext.find_element_by_tag_name('h5').text
        imageUrl = mainContext.find_element_by_class_name('yjl_fx168_news_listPhoto')\
            .find_element_by_tag_name('a').find_element_by_tag_name('img').get_attribute('lazy-src')
        linkUrl = mainContext.find_element_by_class_name('yjl_fx168_news_listTitle')\
            .find_element_by_tag_name('a').get_attribute('href')
        title = mainContext.find_element_by_class_name('yjl_fx168_news_listTitle')\
            .find_element_by_tag_name('a').text
        descriptContext = mainContext.find_element_by_class_name('del').text
        currentList.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'FUTURE','FXNET'])
    return currentList
    
def writeMorningFutureDailyNews():
    link = 'http://news.fx168.com/top/future/'
    currentArray = crawMorningFutureDailyNews(link)
    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  MORNING_OTHERNEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'FXNET' AND  NEWSFLAG='FUTURE'"
    dbManager.executeUpdateOrDelete(SQL)


    formatSQL = ' INSERT MORNING_OTHERNEWS_RESOURCE_TABLE ' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)