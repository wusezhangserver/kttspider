from selenium import webdriver
from commonutils_spider  import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium.common.exceptions import NoSuchElementException
import uuid

def crawMorningForexDailyNews(link):
    currentList = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    contextList = browsor.find_elements_by_class_name('articleItem')
    for context in contextList:
        try:
            linkUrl = context.find_element_by_class_name('img').get_attribute('href')
            imageUrl = context.find_element_by_class_name('img').find_element_by_tag_name('img').get_attribute('src')
            title = context.find_element_by_class_name('title').text
            pubDate = CommonsInitValue.initNowTime()
            descriptContext = context.find_element_by_tag_name('p').text
        except NoSuchElementException,e:
            continue
        currentList.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'FOREX','INVESTINGNET'])
    return currentList

def writeMorningForexDailyNews():
    link = 'http://cn.investing.com/news/%E7%BB%BC%E5%90%88%E6%80%A7%E6%96%B0%E9%97%BB'
    currentArray = crawMorningForexDailyNews(link)
    dbManager = CommonsMysqlUtils._dbManager
    SQL ="DELETE  FROM  MORNING_OTHERNEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'INVESTINGNET' AND  NEWSFLAG='FOREX'"
    dbManager.executeUpdateOrDelete(SQL)
    formatSQL = ' INSERT MORNING_OTHERNEWS_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    writeMorningForexDailyNews()
