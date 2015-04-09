import time
from commonutils_spider import CommonsMysqlUtils
from  selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def searchHexunBlog(link,id):
    blogList = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    currentList = browsor.find_elements_by_class_name('Article')
    for obj in currentList:
        descriptContext = obj.find_element_by_class_name('ArticleSubstanceText').text
        imageUrl = ''
        titleDiv = obj.find_element_by_class_name('ArticleTitleText') \
                      .find_element_by_tag_name('a')
        linkUrl = titleDiv.get_attribute('href')
        title = obj.find_element_by_class_name('ArticleTitle').text
        pubDate = time.strftime("%Y-%m-%d %X",time.localtime())
        try:
            imageUrl = obj.find_element_by_class_name('ArticleSubstanceText')\
                          .find_element_by_tag_name('img')\
                          .get_attribute('src')
        except NoSuchElementException,e:
              continue
        blogList.append([id,title,linkUrl,pubDate,descriptContext,imageUrl])
    return blogList

def writeHexunBlog():
    dbManager = CommonsMysqlUtils._dbManager
    SQL = 'DELETE FROM  DAILYBLOG_FOREXRESOURCE_DETAIL_TABLE'
    dbManager.executeUpdateOrDelete(SQL)

    SELECTSQL = " SELECT CJXJ.LINKURL , CJXJ.ID  FROM" \
                " DAILYBLOG_AUTHOR_RESOURCE_TABLE CJXJ WHERE CJXJ.NET_FL='hexun' "
    rows = dbManager.selectMany(SELECTSQL)

    for row in rows:
        currentReult = searchHexunBlog(row[0],row[1])
        formatSQL = ' INSERT  INTO  DAILYBLOG_FOREXRESOURCE_DETAIL_TABLE ' \
                    ' (ID,TITLE,LINKURL,PUBDATE,DESCRIPTCONTEXT,IMAGEURL)' \
                    ' VALUES (%s,%s,%s,%s,%s,%s)'
        dbManager.executeManyInsert(formatSQL,currentReult)
    
    
    
    
    
    
    