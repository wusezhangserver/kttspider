from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import uuid
import HeXunForexImageDetailSpider


def crawHeXunForexImage(link,keyList):
    currentArray =[]
    detaiArray=[]
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    imageList = browsor.find_element_by_class_name('tupianpindao')
    mainList = imageList.find_elements_by_tag_name('div')
    for context in mainList:
        try:
            linkObj = context.find_element_by_tag_name('a')
            linkUrl = linkObj.get_attribute('href')
            imageUrl = context.find_element_by_tag_name('img').get_attribute('src')
            pubDate = CommonsInitValue.splitCreateDate(linkUrl,'/',3)
            descriptContext = context.find_element_by_tag_name('p').text
            if not (imageUrl in keyList):
                mianId = str(uuid.uuid1())
                currentArray.append([mianId,imageUrl,linkUrl,pubDate,'HEXUNFOREXNET',descriptContext])
                detaiArray.append([mianId,linkUrl])
        except NoSuchElementException,e:
            continue
    HeXunForexImageDetailSpider.writeHeXunForexImageDetail(detaiArray)
    return currentArray

def writeHeXunForexImage():
    link = 'http://forex.hexun.com/pic/'
    dbManager = CommonsMysqlUtils._dbManager
    selectSQL = " SELECT  RESOURCE.IMAGEURL  " \
                " FROM  FOREXPIC_PICTURE_RESOURCE_TABLE RESOURCE" \
                " WHERE 1=1  AND RESOURCE.SOURCEFLAG ='HEXUNFOREXNET' "
    selectDict =dbManager.selectDictMany(selectSQL)
    keyList = []
    for current_dict in selectDict:
            for (key,value) in current_dict.iteritems():
                keyList.append(value)

    currentArray = crawHeXunForexImage(link,keyList)
    formatSQL = ' INSERT INTO  FOREXPIC_PICTURE_RESOURCE_TABLE(ID,IMAGEURL,LINKURL,PUBDATE,SOURCEFLAG,DISCRIPTIONTEXT)' \
                ' VALUES(%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)
