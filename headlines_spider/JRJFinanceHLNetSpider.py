import uuid
from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver


def crawFinanceHLDataSource(link):
    currentList = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    maincontext = browsor.find_element_by_class_name('diss')
    linkUrl = maincontext.find_element_by_tag_name('a').get_attribute('href')
    imageUrl = maincontext.find_element_by_tag_name('img').get_attribute('src')
    contextlist = maincontext.find_element_by_class_name('xh_dis').find_elements_by_tag_name('li')
    title = contextlist[0].text
    descriptContext = contextlist[1].text
    pubDate = CommonsInitValue.initNowTime()
    currentList.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'MACRO','JRJCHINA'])
    return currentList
     
def writeFinanceHLDataSource():
    link = 'http://finance.jrj.com.cn/'
    currentArray = crawFinanceHLDataSource(link)

    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  HEADLINE_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'JRJCHINA'"
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = ' INSERT HEADLINE_FINANCENEWS_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    writeFinanceHLDataSource()