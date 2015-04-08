from  selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from commonutils_spider import CommonsMysqlUtils
import time
import uuid

def crawMorningDailyNews(link):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainContext = browsor.find_element_by_id('search-result')
    listContext = mainContext.find_elements_by_class_name('news')
    for  context in listContext:
         title = context.find_element_by_class_name('title').text
         linkUrl = context.find_element_by_class_name('title').get_attribute('href')
         imageUrl = context.find_element_by_tag_name('img').get_attribute('data-original').split('!')[0]
         pubDate = time.strftime("%Y-%m-%d %X",time.localtime())
         descriptContext = ''
         currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'STOCK','HEJNET'])

    return currentArray


def writeMorningDailyNews():
    link = 'http://wallstreetcn.com/news?cid=17'
    currentArray =  crawMorningDailyNews(link)
    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'HEJNET'  AND  NEWSFLAG='STOCK' "
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = ' INSERT MORNING_FINANCENEWS_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)
    
if __name__=='__main__':
    writeMorningDailyNews()