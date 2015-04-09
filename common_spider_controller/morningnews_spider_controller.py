from mornnews_spider import HEJNewsNetSpider
from mornnews_spider import NBDNewsNetSpider
from mornnews_spider import FXNewsForexNetSpider
from mornnews_spider import FXNewsMetalNetSpider
from mornnews_spider import FXNewsFutureNetSpider
from mornnews_spider import FXNewsStockNetSpider
from mornnews_spider import TakNewsStockNetSpider
from mornnews_spider import YiCaiStockNetSpider
from mornnews_spider import CNNewsNetSpider
from mornnews_spider import XQNewsNetSpider
from mornnews_spider import QQNewsNetSpider
from mornnews_spider import YiCaiFinanceNetSpider
from mornnews_spider import QJNewsStockNetSpider
from mornnews_spider import HTNewsNetSpider
from mornnews_spider import CXNewsNetSpider

def crawDailyNews():
    
    # CRAW HEJNEWS COMMENTS NEWS SIPDER
    #print '----START CRAW HEJNEWS NEWS----'
    #HEJNewsNetSpider.writeMorningDailyNews()
    
    # CRAW QQNEWS COMMENTS NEWS SIPDER
    print '----START CRAW QQNEWS NEWS----'
    try:
        QQNewsNetSpider.writeMorningQQDailyNews()
    except Exception,e:
        print e
    # CRAW NBDNEWS COMMENTS NEWS SIPDER
    print '----START CRAW NBDNEWS NEWS----'
    NBDNewsNetSpider.writeMorningDailyNews()
    
    # CRAW FXNEWS COMMENTS NEWS SIPDER
    print '----START CRAW FXNEWS NEWS----'
    FXNewsForexNetSpider.writeMorningForexDailyNews()

    # CRAW FXNEWSMETAL COMMENTS NEWS SIPDER
    print '----START CRAW FXNEWSMETAL NEWS----'
    FXNewsMetalNetSpider.writeMorningMetalDailyNews() 
    
    # CRAW FXNEWSFUTURE COMMENTS NEWS SIPDER
    print '----START CRAW FXNEWSFUTURE NEWS----'
    FXNewsFutureNetSpider.writeMorningFutureDailyNews()
    
    # CRAW FXNEWSSTOCK COMMENTS NEWS SIPDER
    print '----START CRAW FXNEWSSTOCK NEWS----'
    FXNewsStockNetSpider.writeMorningStockDailyNews()
    
    # CRAW TAKNEWSSTOCK COMMENTS NEWS SIPDER
    print '----START CRAW TAKNEWSSTOCK NEWS----'
    TakNewsStockNetSpider.writeFinanceHLDataSource()
    
    # CRAW YICAISTOCK COMMENTS NEWS SIPDER
    print '----START CRAW YICAISTOCK NEWS----'
    YiCaiStockNetSpider.writeYiCaiStockDataSource()
    
    # CRAW 21CNNEWS NEWS SIPDER
    print '----START CRAW 21CNNEWS NEWS----'
    CNNewsNetSpider.writeCNStockNetDailyNews()

    # CRAW XQ NEWS SIPDER #
    print '----START CRAW XQ NEWS----'
    XQNewsNetSpider.writeXQNewsNetDataSource()

    # CRAW YICAI NEWS SIPDER #
    print  '----START CRAW YCFINANCE NEWS----'
    YiCaiFinanceNetSpider.writeFinanceHLDataSource()

    # CRAW QJ STOCK NEWS SIPDER #
    print  '----START CRAW QJ STOCK NEWS----'
    QJNewsStockNetSpider.writeMorningQJDailyStockNews()

    print '----START CRAW HT FOREX NEWS----'
    HTNewsNetSpider.writeMorningForexDailyNews()

    print '----START CRAW CX STOCK NEWS----'
    CXNewsNetSpider.writeMorningDailyNews()

