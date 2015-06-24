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
from commonutils_spider import CommonsRecodeErrorUtils
from commonutils_spider import CommonsInitValue
import uuid

def crawDataCenter():

    currentList = []
    currentTime = CommonsInitValue.initNowTime()

    # CRAW FOREXGOLD DATA SIPDER
    print '----START CRAW FOREXGOLD DATA----'
    try:
       ForexGoldDataNetSpider.writeForexGoldDataSource()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'ForexGoldDataNetSpider.writeForexGoldDataSource()',e])
    
    # CRAW MARKETSENTIMENT DATA SIPDER
    print '----START CRAW MARKETSENTIMENT DATA----'
    try:
        MarketSentimentDataNetSpider.writeMarketSentimentDataSource()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'MarketSentimentDataNetSpider.writeMarketSentimentDataSource',e])
    
    # CRAW STOCKACCOUNT DATA SIPDER
    print '----START CRAW STOCKACCOUNT DATA----'
    #StockAccountDataNetSpider.writeStockAccountDataCenter()

    # CRAW TRADEACTIVITY DATA SIPDER
    print '----START CRAW TRADEACTIVITY DATA----'
    #TradeActivityDataNetSpider.writeTradeActivityDataCenter()
    
    # CRAW MarginTrade DATA SIPDER
    print '----START CRAW MarginTrade DATA----'
    try:
        MarginTradeDataNetSpider.writeMarginTradeDataSource()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'MarginTradeDataNetSpider.writeMarginTradeDataSource',e])

    # CRAW INDEXFUTURE DATA SIPDER
    print '----START CRAW INDEXFUTURE DATA----'
    try:
        IndexFutureDataNetSpider.writeIndexFutureDataSource()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'IndexFutureDataNetSpider.writeIndexFutureDataSource',e])

    #CRAW THE BULKCARGOTRANS DATA
    print '----START CRAW THE BULKCARGOTRANS DATA----'
    try:
        BulkCargoTransDataNetSpider.writeBulkCargoTransDataSource()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'BulkCargoTransDataNetSpider.writeBulkCargoTransDataSource',e])

    #CRAW THE SHIBOR DATA
    print '----START CRAW THE SHIBOR DATA----'
    try:
       shiborDataNetSpider.writeShiborConceptDataSource()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'shiborDataNetSpider.writeShiborConceptDataSource',e])

    #CRAW THE LPR DATA
    print '-----START CRAW THE LPR DATA-----'
    try:
        LPRDataNetSpider.writeLPRConceptDataSource()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'LPRDataNetSpider.writeLPRConceptDataSource',e])

    #CRAW THE PMI DATA#
    print '-----START CRAW THE PMI DATA-----'
    try:
        PMIDataNetSpider.writePMIDataSource()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'PMIDataNetSpider.writePMIDataSource',e])

    #CRAW THE SOCIALPOWER#
    print '-----START CRAW THE SOCIALPOWER DATA-----'
    try:
        SocialPowerDataNetSpider.writeSocialPowerDataSource()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'SocialPowerDataNetSpider.writeSocialPowerDataSource',e])

    #CRAW THE DOLLARINDEX#
    print '-----START CRAW THE DOLLARINDEX DATA-----'
    try:
        DollarIndexDataNetSpider.writeDollarIndexDataSource()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'DollarIndexDataNetSpider.writeDollarIndexDataSource',e])

    CommonsRecodeErrorUtils.commonRedcodeError(currentList)
