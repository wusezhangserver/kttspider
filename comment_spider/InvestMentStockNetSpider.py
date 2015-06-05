from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
import uuid


def crawDailyStockComments(link):
    currentArray =[]
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainlist = browsor.find_element_by_id('investmenttbl').find_elements_by_tag_name('tr')
    for context in mainlist:
        print ''


    #currentArray.append([str(uuid.uuid1()),linkUrl,title,pubDate,descriptContext,'STOCK','INVESTMENT'])
    return currentArray

def writeDailyStockComments():
    link = 'http://moer.jiemian.com/investment.htm'
    currentArray = crawDailyStockComments(link)

    #dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  COMMENTS_STOCK_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'INVESTMENT'"
    #dbManager.executeUpdateOrDelete(SQL)

    formatSQL = ' INSERT COMMENTS_STOCK_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,TITLE,PUBDATE,DESCRIPTCONTEXT,COMMENTFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s)'
    #dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    writeDailyStockComments()