from selenium import webdriver
from commonutils_spider  import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium.common.exceptions import NoSuchElementException
import uuid

def crawMorningMetalDailyNews(link):
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
        currentList.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'METAL','INVESTINGNET'])
    return currentList

def writeMorningMetalDailyNews():
    link = 'http://cn.investing.com/news/%E5%95%86%E5%93%81-%E6%9C%9F%E8%B4%A7%E6%96%B0%E9%97%BB'
    currentArray = crawMorningMetalDailyNews(link)
    print currentArray
    dbManager = CommonsMysqlUtils._dbManager
    SQL ="DELETE  FROM  MORNING_OTHERNEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'INVESTINGNET' AND  NEWSFLAG='METAL'"
    dbManager.executeUpdateOrDelete(SQL)
    formatSQL = ' INSERT MORNING_OTHERNEWS_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)


if __name__ == '__main__':
    writeMorningMetalDailyNews()