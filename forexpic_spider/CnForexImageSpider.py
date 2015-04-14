from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver
import uuid

def crawCnForexImages(link,keyList):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    imageList = browsor.find_elements_by_class_name('imgModel')
    for model in imageList:
        linkUrl = model.find_element_by_tag_name('a').get_attribute('href')
        imageUrl = model.find_element_by_tag_name('img').get_attribute('src')
        pubDate = CommonsInitValue.returnCreateDate(model.find_element_by_tag_name('p').text)
        if not (imageUrl in keyList):
            mianId = str(uuid.uuid1())
            currentArray.append([mianId,imageUrl,linkUrl,pubDate,'CNFOREXNET'])
    return currentArray
        
def writeForexImages():
    link = 'http://www.cnforex.com/news/tuce/'
    dbManager = CommonsMysqlUtils._dbManager
    selectSQL = " SELECT  RESOURCE.IMAGEURL  " \
                " FROM  FOREXPIC_PICTURE_RESOURCE_TABLE RESOURCE WHERE 1=1 "
    selectDict =dbManager.selectDictMany(selectSQL)
    keyList = []
    for current_dict in selectDict:
            for (key,value) in current_dict.iteritems():
                keyList.append(value)

    currentArray = crawCnForexImages(link,keyList)
    formatSQL = ' INSERT INTO  FOREXPIC_PICTURE_RESOURCE_TABLE(ID,IMAGEURL,LINKURL,PUBDATE,SOURCEFLAG)' \
                ' VALUES(%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    writeForexImages()