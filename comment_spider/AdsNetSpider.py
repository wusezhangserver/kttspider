from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
import uuid

def crawDailyComments(link):

    currentList = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    contextList = browsor.find_elements_by_class_name('news-item')
    for mainContext in contextList:
        pubDate = CommonsInitValue.initNowTime()
        title = mainContext.find_element_by_tag_name('a').text
        linkUrl = mainContext.find_element_by_tag_name('a').get_attribute('href')
        descriptContext = mainContext.find_element_by_class_name('desc').text
        currentList.append([str(uuid.uuid1()),linkUrl,title,pubDate,descriptContext,'FOREX','ADSNET'])
    return currentList


def writeDailyComments():
    link = 'http://www.ads-securities.com/zhs/market-research'
    currentArray = crawDailyComments(link)

    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  COMMENTS_NEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'ADSNET' AND COMMENTFLAG='FOREX' "
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = ' INSERT COMMENTS_NEWS_RESOURCE_TABLE ' \
                ' (KEYID,LINKURL,TITLE,PUBDATE,DESCRIPTCONTEXT,COMMENTFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    writeDailyComments()