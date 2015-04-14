from commonutils_spider import CommonsMysqlUtils
from commonutils_spider import CommonsInitValue
from selenium import webdriver



def crawCnForexImageDetail(link,id):
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainContext = browsor.find_elements_by_class_name('thumbnailimage')
    for context in mainContext:
        mainInfor = context.find_element_by_class_name('large_image')
        descriptContext =mainInfor.get_attribute('rel')
        imageUrl = mainInfor.get_attribute('src')
        print imageUrl+':'+descriptContext


def writeCnForexImageDetail():
    links ='http://www.cnforex.com/news/tuce/show.aspx?c=431'
    crawCnForexImageDetail(links,'')

if __name__ == '__main__':
    writeCnForexImageDetail()