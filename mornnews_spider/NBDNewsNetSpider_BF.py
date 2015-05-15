from  selenium import webdriver
from commonutils_spider import CommonsMysqlUtils
import uuid


def crawMorningDailyNews(linkUrl):
    currentList = []
    browsor = webdriver.PhantomJS()
    browsor.get(linkUrl)
    resultList = browsor.find_elements_by_class_name('mt24')
    print resultList
    for div in resultList:
        imageUrl = div.find_element_by_class_name('macroscopic-img').find_element_by_tag_name('img').get_attribute('src')
        print imageUrl

    ##currentList.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'CHINA','NBDNET'])
    return currentList


def writeMorningDailyNews():
    linkUrl = 'http://www.nbd.com.cn/columns/3'
    currentArray = crawMorningDailyNews(linkUrl)
    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'NBDNET'"
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = 'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    linkUrl = 'http://www.nbd.com.cn/columns/3'
    crawMorningDailyNews(linkUrl)