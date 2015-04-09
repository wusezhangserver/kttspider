from datacenter_spider import ForexGoldDataNetSpider
from datacenter_spider import MarketSentimentDataNetSpider
from datacenter_spider import StockAccountDataNetSpider
from datacenter_spider import TradeActivityDataNetSpider
from datacenter_spider import IndexFutureDataNetSpider
from datacenter_spider import BulkCargoTransDataNetSpider
from datacenter_spider import shiborDataNetSpider
from datacenter_spider import LPRDataNetSpider
from datacenter_spider import PMIDataNetSpider
from datacenter_spider import SocialPowerDataNetSpider
from datacenter_spider import DollarIndexDataNetSpider
from datacenter_spider import MarginTradeDataNetSpider

def  crawDataCenter():

    # CRAW FOREXGOLD DATA SIPDER
    print '----START CRAW FOREXGOLD DATA----'
    ForexGoldDataNetSpider.writeForexGoldDataSource()
    
    # CRAW MARKETSENTIMENT DATA SIPDER
    print '----START CRAW MARKETSENTIMENT DATA----'
    MarketSentimentDataNetSpider.writeMarketSentimentDataSource()
    
    # CRAW STOCKACCOUNT DATA SIPDER
    print '----START CRAW STOCKACCOUNT DATA----'
    #StockAccountDataNetSpider.writeStockAccountDataCenter()

    # CRAW TRADEACTIVITY DATA SIPDER
    print '----START CRAW TRADEACTIVITY DATA----'
    #TradeActivityDataNetSpider.writeTradeActivityDataCenter()
    
    # CRAW MarginTrade DATA SIPDER
    print '----START CRAW MarginTrade DATA----'
    MarginTradeDataNetSpider.writeMarginTradeDataSource()

    # CRAW INDEXFUTURE DATA SIPDER
    print '----START CRAW INDEXFUTURE DATA----'
    IndexFutureDataNetSpider.writeIndexFutureDataSource()

    #CRAW THE BULKCARGOTRANS DATA
    print '----START CRAW THE BULKCARGOTRANS DATA----'
    BulkCargoTransDataNetSpider.writeBulkCargoTransDataSource()

    #CRAW THE SHIBOR DATA
    print '----START CRAW THE SHIBOR DATA----'
    shiborDataNetSpider.writeShiborConceptDataSource()

    #CRAW THE LPR DATA
    print '-----START CRAW THE LPR DATA-----'
    LPRDataNetSpider.writeLPRConceptDataSource()

    #CRAW THE PMI DATA#
    print '-----START CRAW THE PMI DATA-----'
    PMIDataNetSpider.writePMIDataSource()

    #CRAW THE SOCIALPOWER#
    print '-----START CRAW THE SOCIALPOWER DATA-----'
    SocialPowerDataNetSpider.writeSocialPowerDataSource()

    #CRAW THE DOLLARINDEX#
    print '-----START CRAW THE DOLLARINDEX DATA-----'
    DollarIndexDataNetSpider.writeDollarIndexDataSource()


if __name__=='__main__':
    crawDataCenter()