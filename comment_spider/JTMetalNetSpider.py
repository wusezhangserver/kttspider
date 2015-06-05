from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
import uuid

def crawDailyMetalComments(link):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainlist = browsor.find_element_by_class_name('xwlistc1').find_elements_by_tag_name('li')
    for context in mainlist:
        title = context.find_element_by_tag_name('a').text
        linkUrl = context.find_element_by_tag_name('a').get_attribute('href')
        pubDate = context.find_element_by_tag_name('span').text
        currentArray.append([str(uuid.uuid1()),linkUrl,title,pubDate,'','METAL','GTNET'])
    return currentArray

def writeDailyMetalComments():

    link = 'http://www.jiatai9999.com/list.php?catId=4'
    currentArray = crawDailyMetalComments(link)

    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  COMMENTS_METAL_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'GTNET'"
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = 'INSERT COMMENTS_METAL_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,TITLE,PUBDATE,DESCRIPTCONTEXT,COMMENTFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)
    
if __name__=='__main__':
    writeDailyMetalComments()
