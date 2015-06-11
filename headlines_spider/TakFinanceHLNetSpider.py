import uuid
from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver

def crawFinanceHLDataSource(link):
    currentList = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    maincontext = browsor.find_element_by_id('news_pic').find_element_by_class_name('changeDiv')
    linkUrl = maincontext.find_element_by_tag_name('a').get_attribute('href')
    title = maincontext.find_element_by_tag_name('a').text
    pubDate = CommonsInitValue.initNowTime()
    imageUrl = maincontext.find_element_by_tag_name('img').get_attribute('src')
    print linkUrl+":"+title+":"+imageUrl
    #currentList.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'MACRO','TAKCHINA'])
    return currentList
     
def writeFinanceHLDataSource():
    link = 'http://finance.takungpao.com/'
    currentList = crawFinanceHLDataSource(link)
    SQL= "DELETE  FROM  HEADLINE_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'TAKCHINA'"
    formatSQL = ' INSERT HEADLINE_FINANCENEWS_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'

if __name__ == '__main__':
    writeFinanceHLDataSource()