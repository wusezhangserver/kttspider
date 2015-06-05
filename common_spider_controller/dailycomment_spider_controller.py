from comment_spider import HuiTongNetSpider
from comment_spider import AdsNetSpider
from comment_spider import GXMetalNetSpider
from comment_spider import JTMetalNetSpider
from comment_spider import SYMetalNetSpider
from comment_spider import ZZStockNetSpider
from comment_spider import HGStockNetSpider
from comment_spider import JFStockNetSpider
from comment_spider import QJStockNetSpider
from comment_spider import QJFinanceNetSpider
from comment_spider import SinaFinanceNetSpider
from comment_spider import QQFinanceNetSpider
from comment_spider import SilverMetalNetSpider
from commonutils_spider import CommonsRecodeErrorUtils
import uuid
import time

def crawCommentsNews():
    
    currentList = []
    currentTime = time.strftime("%Y-%m-%d %X",time.localtime());
    

    # CRAW AdsNet COMMENTS NEWS SIPDER
    print '----START CRAW AdsNet COMMENTS NEWS----'
    try:
        AdsNetSpider.writeDailyComments()
    except Exception ,e: 
        currentList.append([currentTime,str(uuid.uuid1()),'AdsNetSpider.writeDailyComments()',e])
     

    # CRAW GXMetal COMMENTS NEWS SIPDER
    print '----START CRAW GXMetal COMMENTS NEWS----'
    try :
        GXMetalNetSpider.writeDailyMetalComments()
    except Exception,e:
        currentList.append([currentTime,str(uuid.uuid1()),' GXMetalNetSpider.writeDailyMetalComments()',e])

    print '----START CRAW ERROR INFORMATION----'

    # CRAW JFStock COMMENTS NEWS SIPDER
    print '----START CRAW JFStock COMMENTS NEWS----'
    try:
        JFStockNetSpider.writeDailyStockComments()
    except Exception,e:
        currentList.append([currentTime,str(uuid.uuid1()),' JFStockNetSpider.writeDailyStockComments()',e])







    print '----START CRAW ERROR INFORMATION----'
    CommonsRecodeErrorUtils.commonRedcodeError(currentList)