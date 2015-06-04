from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
import uuid


def crawDailyMetalComments(link):
    currentArray =[]
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    contextList = browsor.find_element_by_class_name('right_box796')\
        .find_element_by_tag_name('ul')\
        .find_elements_by_tag_name('li')
    for context in contextList:
        pubDate = context.find_element_by_class_name('time').text
        title = context.find_element_by_tag_name('a').text
        linkUrl = context.find_element_by_tag_name('a').get_attribute('href')
        descriptContext = CommonsInitValue.removeSpecialCharacter(context.text)
        currentArray.append([str(uuid.uuid1()),linkUrl,title,pubDate,descriptContext,'METAL','GXNET'])
    return currentArray
    

def writeDailyMetalComments():
    link = 'http://www.91jin.com/gxrp.html'
    currentArray = crawDailyMetalComments(link)
    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  COMMENTS_METAL_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'GXNET' AND COMMENTFLAG='METAL' "
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = 'INSERT COMMENTS_METAL_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,TITLE,PUBDATE,DESCRIPTCONTEXT,COMMENTFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)
    
if __name__=='__main__':
    writeDailyMetalComments()