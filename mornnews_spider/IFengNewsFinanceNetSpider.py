from selenium import webdriver
from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
import uuid

def crawMorningFinanceDailyNews(linkUrl):
    currentArray=[]
    browsor = webdriver.PhantomJS()
    browsor.get(linkUrl)
    mainList = browsor.find_element_by_id('list01').find_elements_by_tag_name('li')
    for context in mainList:
        linkUrl = context.find_element_by_tag_name('a').get_attribute('href')
        title = context.find_element_by_tag_name('a').text
        pubDate = context.find_element_by_class_name('date').text
        descriptContext = context.find_element_by_tag_name('p').text
        imageUrl = CommonsInitValue.initTempImage()
        currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'CHINA','IFengNET'])
    return currentArray


def writeMorningFinanceDailyNews():
    link = 'http://finance.ifeng.com/macro/policy/'
    currentArray = crawMorningFinanceDailyNews(link)
    dbManager = CommonsMysqlUtils._dbManager
    SQL = " DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'IFengNET' " \
          " AND  NEWSFLAG='CHINA' "
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = 'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    writeMorningFinanceDailyNews()

