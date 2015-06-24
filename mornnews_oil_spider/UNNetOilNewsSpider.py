from selenium import webdriver
from commonutils_spider import CommonsInitValue
from selenium.common.exceptions import NoSuchElementException
import uuid


def crawMorningOilDailyNews(linkUrl):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(linkUrl)
    mainlist = browsor.find_element_by_id('table').find_elements_by_class_name('evenrow')
    for context in mainlist:
        linkUrl = context.find_element_by_tag_name('a').get_attribute('href')
        title = context.find_element_by_tag_name('a').text
        pubDate = CommonsInitValue.initNowTime()
        if title =='':
            continue
        print title+":"+linkUrl


def writeMorningOilDailyNews():
    link = 'http://unews.fx678.com/union/ifx/gzys.html'
    currentArray = crawMorningOilDailyNews(link)
    #dbManager = CommonsMysqlUtils._dbManager
    SQL = " DELETE  FROM  MORNING_OILNEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'YHOIL' " \
          " AND  NEWSFLAG='OIL' "
    #dbManager.executeUpdateOrDelete(SQL)

    formatSQL = 'INSERT MORNING_OILNEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    #dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    writeMorningOilDailyNews()