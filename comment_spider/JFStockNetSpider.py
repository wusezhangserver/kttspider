from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
import uuid


def crawDailyStockComments(link):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainlist = browsor.find_element_by_class_name('w_660')\
        .find_element_by_tag_name('ul')\
        .find_elements_by_tag_name('li')
    for context in mainlist:
        title = context.find_element_by_tag_name('a').text
        linkUrl = context.find_element_by_tag_name('a').get_attribute('href')
        descriptContext = context.find_element_by_tag_name('p').text
        pubDate = CommonsInitValue.initNowTime()
        currentArray.append([str(uuid.uuid1()),linkUrl,title,pubDate,descriptContext,'STOCK','JFNET'])
    return currentArray

    
def writeDailyStockComments():    
    link = 'http://research.jfinfo.com/jfyj/'
    currentArray = crawDailyStockComments(link)

    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  COMMENTS_STOCK_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'JFNET'"
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = ' INSERT COMMENTS_STOCK_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,TITLE,PUBDATE,DESCRIPTCONTEXT,COMMENTFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    writeDailyStockComments()