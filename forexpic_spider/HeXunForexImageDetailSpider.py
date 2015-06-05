from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import uuid

def crawHeXunForexImageDetail(link,id):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    imageList = browsor.find_element_by_id('smallPicList')
    contextList = imageList.find_elements_by_tag_name('li')
    for context in contextList:
        linkUrl = context.find_element_by_tag_name('a').get_attribute('href')
        imageUrl = context.find_element_by_tag_name('img').get_attribute('src')
        currentArray.append([str(uuid.uuid1()),id,imageUrl,''])
    return currentArray

def writeHeXunForexImageDetail(detailArray):
    dbManager = CommonsMysqlUtils._dbManager
    SQL ='INSERT  INTO FOREXPIC_PICDETAIL_RESOURCE_TABLE (ID,PID,IMAGEURL,DISCRIPTIONCONTEXT) VALUES(%s,%s,%s,%s)'
    for obj in detailArray:
        list = crawHeXunForexImageDetail(obj[1],obj[0])
        print list
        dbManager.executeManyInsert(SQL,list)