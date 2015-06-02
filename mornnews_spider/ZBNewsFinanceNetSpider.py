from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import uuid

def crawZBNewsNetDataSource(link):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    contextList = browsor.find_elements_by_class_name('l_title')
    for context in contextList:
        pubDate = CommonsInitValue.initNowTime()
        try:
            imageUrl = context.find_element_by_tag_name('img').get_attribute('src')
        except NoSuchElementException,e:
            imageUrl = CommonsInitValue.initTempImage()
        title = context.find_element_by_class_name('title').text
        descriptContext = context.find_element_by_class_name('text').text
        linkUrl = context.find_element_by_tag_name('a').get_attribute('href')
        currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'CHINA','ZBNET'])
    return currentArray


def writeZBNewsNetDataSource():
    link = 'http://www.zaobao.com/finance/china'
    currentArray = crawZBNewsNetDataSource(link)
    dbManager = CommonsMysqlUtils._dbManager
    SQL = " DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'ZBNET' " \
          " AND  NEWSFLAG='CHINA' "
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = 'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)


