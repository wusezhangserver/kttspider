from selenium import webdriver
from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
import uuid

def crawFinanceHLDataSource(link):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainlist = browsor.find_element_by_class_name('news_list').find_elements_by_class_name('list')


    #currentList.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'STOCK','TAKCHINA'])
    return currentArray
     
def writeFinanceHLDataSource():
    link = 'http://finance.takungpao.com/'
    currentList = crawFinanceHLDataSource(link)
    SQL = "DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'TAKCHINA' AND  NEWSFLAG='STOCK'"

    formatSQL = 'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'

if __name__ == '__main__':
    writeFinanceHLDataSource()