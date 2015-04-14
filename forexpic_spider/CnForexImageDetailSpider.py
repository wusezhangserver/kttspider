from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
import uuid


def crawCnForexImageDetail(link,id):
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    currentArray = []
    mainContext = browsor.find_elements_by_class_name('thumbnailimage')
    for context in mainContext:
        mainInfor = context.find_element_by_class_name('large_image')
        descriptContext =mainInfor.get_attribute('rel')
        imageUrl = mainInfor.get_attribute('src')
        currentArray.append([str(uuid.uuid1()),id,imageUrl,descriptContext])
    return currentArray

def writeCnForexImageDetail(detailArray):
    dbManager = CommonsMysqlUtils._dbManager
    SQL ='INSERT  INTO FOREXPIC_PICDETAIL_RESOURCE_TABLE (ID,PID,IMAGEURL,DISCRIPTIONCONTEXT) VALUES(%s,%s,%s,%s)'
    for obj in detailArray:
        print obj[1]+':'+obj[0]
        list = crawCnForexImageDetail(obj[1],obj[0])
        dbManager.executeManyInsert(SQL,list)