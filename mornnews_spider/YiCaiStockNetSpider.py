from commonutils_spider import  CommonsMysqlUtils
from  selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def crawYiCaiStockDailyNews(link):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    contextArray = browsor.find_elements_by_tag_name('dl')
    for context in contextArray:
        title = context.find_element_by_tag_name('h1').text
        print title





    #currentList.append([str(uuid.uuid1()),linkUrl,topImageUrl,title,pubDate,descriptContext,'STOCK','YICAINET'])
    return currentArray
    
def writeYiCaiStockDataSource():
    link = 'http://www.yicai.com/stock/'
    currentArray = crawYiCaiStockDailyNews(link)
    SQL = " DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE" \
           "  WHERE  SOURCEFLAG = 'YICAINET' AND  NEWSFLAG='STOCK'"

    formatSQL = 'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG) ' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'

if __name__ == '__main__':
    writeYiCaiStockDataSource()