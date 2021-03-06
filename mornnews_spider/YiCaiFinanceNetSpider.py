import  time
import  uuid
from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from  selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def crawYCFinanceHLDataSource(link):
    listArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    courrentContext = browsor.find_elements_by_tag_name('dl')

    for currentDiv in  courrentContext:
         try:
              titleObj = currentDiv.find_element_by_tag_name('h1')
              title = titleObj.text
              linkUrl = titleObj.find_element_by_tag_name('a').get_attribute('href')
              descriptContext = currentDiv.find_element_by_tag_name('p').text
              pubDate = CommonsInitValue.initNowTime()
              try:
                  imageObj = currentDiv.find_element_by_tag_name('img')
                  imageUrl = imageObj.get_attribute('src')
              except NoSuchElementException,e:
                  imageUrl = CommonsInitValue.initTempImage()
         except NoSuchElementException,e:
              continue
         listArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'CHINA','YCNET'])
    return listArray

def writeFinanceHLDataSource():
    link = 'http://www.yicai.com/finance/'

    dbManager = CommonsMysqlUtils._dbManager
    SQL = " DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'YCNET' " \
          " AND  NEWSFLAG='CHINA' "
    dbManager.executeUpdateOrDelete(SQL)

    currentArray = crawYCFinanceHLDataSource(link)
    formatSQL = 'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)


if __name__=='__main__':
    writeFinanceHLDataSource()