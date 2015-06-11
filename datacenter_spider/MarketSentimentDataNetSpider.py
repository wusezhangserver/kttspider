from  selenium import webdriver
from commonutils_spider import CommonsSpiderUtils
import json

def crawMarketSentimentDataSource(link):
    currentArray = []
    text = CommonsSpiderUtils.openInternetUrl(link)
    text = CommonsSpiderUtils.removeSpecialCharacter(text)

    return currentArray

def writeMarketSentimentDataSource():
    link = 'http://www.wlstock.com/ajaxRequrst/AllFeelingAjax.ashx?type=2&sd=&ed=&t1=11'
    currentArray = crawMarketSentimentDataSource(link)
    SQL = "DELETE  FROM  DATACENTER_MARKETSENTIMENT_RESOURCE_TABLE"
    formatSQL = 'INSERT INTO  DATACENTER_MARKETSENTIMENT_RESOURCE_TABLE' \
                '(CURRENTDATE,CURRENTVALUE,DESCRIPTCONTEXT) VALUES (%s,%s,%s)'

if __name__ == '__main__':
    writeMarketSentimentDataSource()