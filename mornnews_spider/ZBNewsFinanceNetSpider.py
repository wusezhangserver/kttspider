from commonutils_spider import  CommonsMysqlUtils
from commonutils_spider import  CommonsInitValue
from  selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def crawZBNewsNetDataSource(link):
    print link


def writeZBNewsNetDataSource():
    link = 'http://www.zaobao.com/finance/china'
    currentArray = crawZBNewsNetDataSource(link)


if __name__ == '__main__':
    writeZBNewsNetDataSource()

