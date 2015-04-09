from commonutils_spider import  CommonsMysqlUtils
import uuid
import time

def crawYiCaiStockDailyNews(link,webNet):
    print link
    #currentList.append([str(uuid.uuid1()),linkUrl,topImageUrl,title,pubDate,descriptContext,'STOCK','YICAINET'])

    
def writeYiCaiStockDataSource():
    link = 'http://www.yicai.com/stock/'
    SQL = " DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE" \
           "  WHERE  SOURCEFLAG = 'YICAINET' AND  NEWSFLAG='STOCK'"

    formatSQL = 'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG) ' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'