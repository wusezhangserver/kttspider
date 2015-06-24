from selenium import webdriver
from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium.common.exceptions import NoSuchElementException
import uuid


def crawMorningOilDailyNews(linkUrl):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(linkUrl)
    maincontext = browsor.find_element_by_class_name('news_list_all').find_elements_by_tag_name('li')
    for context in maincontext:
        imageUrl = CommonsInitValue.initoiltempimage()
        descriptContext = context.find_element_by_tag_name('p').text
        linkUrl = context.find_element_by_tag_name('a').get_attribute('href')
        title = context.find_element_by_tag_name('a').text
        pubDate = CommonsInitValue.initNowTime()
        currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'OIL','XIDU'])
    return currentArray


def writeMorningOilDailyNews():
    link = 'http://www.xiduoil.com/jingxuanhangqing/'
    currentArray = crawMorningOilDailyNews(link)
    dbManager = CommonsMysqlUtils._dbManager
    SQL = " DELETE  FROM  MORNING_OILNEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'XIDU' " \
          " AND  NEWSFLAG='OIL' "
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = 'INSERT MORNING_OILNEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    writeMorningOilDailyNews()