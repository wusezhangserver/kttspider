from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
import uuid

def crawDailyComments(link):
    currentArray = []
    ## currentList.append([str(uuid.uuid1()),linkUrl,title,pubDate,descriptContext,'FOREX','FOREXNET'])

    return currentArray


def writeDailyComments():
    link = 'http://www.forex.com/uk/cns/public-market-updates.html'
    currentArray = crawDailyComments(link)
    SQL = "DELETE  FROM  COMMENTS_NEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'FOREXNET'"
    dbManager = CommonsMysqlUtils._dbManager
    dbManager.executeUpdateOrDelete(SQL)
    formatSQL = 'INSERT COMMENTS_NEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,TITLE,PUBDATE,DESCRIPTCONTEXT,COMMENTFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)



if __name__=='__main__':
    writeDailyComments()