import  time
import  uuid
import sys
sys.path.append("../commonutils_spider/")
import CommonsMysqlUtils
from  selenium import webdriver


def crawJMHotMarketDataSource(link):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainContext = browsor.find_element_by_id('investmenttbl')
    contextList = mainContext.find_elements_by_tag_name('tr')
    for div in  contextList:
        linkUrl = div.find_element_by_tag_name('a').get_attribute('href')
        title = div.find_element_by_tag_name('a').text
        descriptContext = div.find_element_by_tag_name('p').text
        pubDate = time.strftime("%Y-%m-%d %X",time.localtime())
        imageUrl =''
        currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'STOCKDAILY','JMNET'])
    return currentArray

def writeJMHotMarketDataSource():

     link = 'http://moer.jiemian.com/scoop.htm?todayRm=todayRm'
     currentList = crawJMHotMarketDataSource(link)

     dbManager = CommonsMysqlUtils._dbManager
     SQL = "DELETE  FROM  HEADLINE_HOTMARKET_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'JMNET'"
     dbManager.executeUpdateOrDelete(SQL)


     formatSQL = 'INSERT HEADLINE_HOTMARKET_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
     dbManager.executeManyInsert(formatSQL,currentList)