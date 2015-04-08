import mornnews_spider.HEJNewsNetSpider
import mornnews_spider.NBDNewsNetSpider
import mornnews_spider.FXNewsForexNetSpider
import mornnews_spider.FXNewsMetalNetSpider
import mornnews_spider.FXNewsFutureNetSpider
import mornnews_spider.FXNewsStockNetSpider
import mornnews_spider.TakNewsStockNetSpider
import mornnews_spider.YiCaiStockNetSpider
import mornnews_spider.CNNewsNetSpider
import mornnews_spider.XQNewsNetSpider
import mornnews_spider.QQNewsNetSpider
import mornnews_spider.YiCaiFinanceNetSpider
import mornnews_spider.QJNewsStockNetSpider
import mornnews_spider.HTNewsNetSpider
import mornnews_spider.CXNewsNetSpider

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

if __name__=='__main__':
    crawDailyNews()
