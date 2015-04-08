import headlines_spider.ForbesFinanceHLNetSpider
import headlines_spider.FortuneFinanceHLNetSpider
import headlines_spider.FTFinanceHLNetSpider
import headlines_spider.TakFinanceHLNetSpider
import headlines_spider.NBDFinanceHLNetSpider
import headlines_spider.CCTVFinanceHLNetSpider
import headlines_spider.JRJFinanceHLNetSpider
import headlines_spider.CXFinanceHLNetSpider
import headlines_spider.JMHotmarketNetSpider

def crawDataCenter():
    
    # CRAW FORBESFINANCE DATA SIPDER
    print '----START CRAW FORBESFINANCE DATA----'
    ForbesFinanceHLNetSpider.writeFinanceHLDataSource()
    
    # CRAW FORTUREFINANCE DATA SIPDER
    print '----START CRAW FORTUREFINANCE DATA----'
    FortuneFinanceHLNetSpider.writeFinanceHLDataSource()
    
    # CRAW FTFINANCEHL DATA SIPDER
    print '----START CRAW FTFINANCEHL DATA----'
    FTFinanceHLNetSpider.writeFinanceHLDataSource()
    
    # CRAW TAKFINANCEHL DATA SIPDER
    print '----START CRAW TAKFINANCEHL DATA----'
    TakFinanceHLNetSpider.writeFinanceHLDataSource()
    
    # CRAW NBDFINANCEHL DATA SIPDER
    print '----START CRAW NBDFINANCEHL DATA----'
    NBDFinanceHLNetSpider.writeFinanceHLDataSource()
    
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

if __name__=='__main__':
    crawDataCenter()  
