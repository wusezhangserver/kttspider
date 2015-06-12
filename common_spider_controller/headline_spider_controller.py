from headlines_spider import ForbesFinanceHLNetSpider
from headlines_spider import FortuneFinanceHLNetSpider
from headlines_spider import FTFinanceHLNetSpider
from headlines_spider import TakFinanceHLNetSpider
from headlines_spider import CCTVFinanceHLNetSpider
from headlines_spider import JRJFinanceHLNetSpider
from headlines_spider import CXFinanceHLNetSpider
from headlines_spider import JMHotmarketNetSpider

def crawDataCenter():
    
    # CRAW FORBESFINANCE DATA SIPDER
    print '----START CRAW FORBESFINANCE DATA----'
    ForbesFinanceHLNetSpider.writeFinanceHLDataSource()
    
    # CRAW FORTUREFINANCE DATA SIPDER
    print '----START CRAW FORTUREFINANCE DATA----'
    FortuneFinanceHLNetSpider.writeFinanceHLDataSource()
    
    # CRAW FTFINANCEHL DATA SIPDER
    print '----START CRAW FTFINANCEHL DATA----'
    try:
        FTFinanceHLNetSpider.writeFinanceHLDataSource()
    except Exception,e:
        print e
    
    # CRAW TAKFINANCEHL DATA SIPDER
    print '----START CRAW TAKFINANCEHL DATA----'
    TakFinanceHLNetSpider.writeFinanceHLDataSource()

    # CRAW CCTVFINANCEHL DATA SIPDER
    print '----START CRAW CCTVFINANCEHL DATA----'
    try:
        CCTVFinanceHLNetSpider.writeFinanceHLDataSource()
    except Exception,e:
        print e

    # CRAW JRJFINANCEHL DATA SIPDER
    print '----START CRAW JRJFINANCEHL DATA----'
    JRJFinanceHLNetSpider.writeFinanceHLDataSource()

    # CRAW CXFinanceHLNet DATA SIPDER
    print '----START CRAW CXFINANCEHLNET DATA----'
    CXFinanceHLNetSpider.writeCXFinanceHLDataSource()

    print '----START CRAW JMHOTMARKET DATA ---'
    JMHotmarketNetSpider.writeJMHotMarketDataSource()

