from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver

def crawCnForexImages(link):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    imageList = browsor.find_elements_by_class_name('imgModel')
    for model in imageList:
        linkUrl = model.find_element_by_tag_name('a').get_attribute('href')
        imageUrl = model.find_element_by_tag_name('img').get_attribute('src')
        pubDate = CommonsInitValue.returnCreateDate(model.find_element_by_tag_name('p').text)
        print linkUrl+':'+imageUrl+':'+pubDate



    return currentArray
        
def writeForexImages():
    link = 'http://www.cnforex.com/news/tuce/'
    currentArray = crawCnForexImages(link)
        
if __name__ == '__main__':
    writeForexImages()