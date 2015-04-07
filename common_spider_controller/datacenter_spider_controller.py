import sys
sys.path.append('../datacenter_spider/')
import ForexGoldDataNetSpider
import MarketSentimentDataNetSpider
import StockAccountDataNetSpider
import TradeActivityDataNetSpider
import IndexFutureDataNetSpider
import BulkCargoTransDataNetSpider
import shiborDataNetSpider
import LPRDataNetSpider
import PMIDataNetSpider
import SocialPowerDataNetSpider
import DollarIndexDataNetSpider
import MarginTradeDataNetSpider

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