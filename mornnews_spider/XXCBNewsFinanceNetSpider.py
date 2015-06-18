from selenium import webdriver
from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium.common.exceptions import NoSuchElementException
import uuid


def crawMorningFinanceDailyNews(linkUrl):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(linkUrl)
    maincontext = browsor.find_element_by_class_name('area_left')\
            .find_elements_by_class_name('list_item')
    for context in maincontext:
        imageUrl = context.find_element_by_tag_name('img').get_attribute('src')
        descriptContext = context.find_element_by_tag_name('p').text
        linkUrl = context.find_element_by_tag_name('a').get_attribute('href')
        title = context.find_element_by_tag_name('h2').text
        pubDate = CommonsInitValue.initNowTime()
        currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'CHINA','XXCB'])
    return currentArray


def writeMorningFinanceDailyNews():
    link = 'http://www.xxcb.cn/event/caijing/'
    currentArray = crawMorningFinanceDailyNews(link)
    dbManager = CommonsMysqlUtils._dbManager
    SQL = " DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'XXCB' " \
          " AND  NEWSFLAG='CHINA' "
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = 'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    writeMorningFinanceDailyNews()