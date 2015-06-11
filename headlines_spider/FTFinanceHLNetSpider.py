import uuid
from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver

def crawFinanceHLDataSource(link):
    currentList = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainContext = browsor.find_element_by_class_name('column11')
    title = mainContext.find_element_by_tag_name('a').text
    linkUrl = mainContext.find_element_by_tag_name('a').get_attribute('href')
    imageUrl = mainContext.find_element_by_tag_name('img').get_attribute('src')
    descriptContext = mainContext.find_element_by_class_name('lead').text
    pubDate = CommonsInitValue.initNowTime()
    currentList.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'MACRO','FTCHINA'])
    return currentList
     
def writeFinanceHLDataSource():
    link = 'http://www.ftchinese.com/'
    currentList = crawFinanceHLDataSource(link)

    dbManager = CommonsMysqlUtils._dbManager
    SQL="DELETE  FROM  HEADLINE_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'FTCHINA'"
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = 'INSERT HEADLINE_FINANCENEWS_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentList)
