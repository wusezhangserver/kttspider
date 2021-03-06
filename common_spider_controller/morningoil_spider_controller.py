from mornnews_oil_spider import XDNetOilNewsSpider
from mornnews_oil_spider import YHNetOilNewsSpider
from commonutils_spider import CommonsRecodeErrorUtils
from commonutils_spider import CommonsInitValue
import uuid


def crawDailyOilNews():

    currentList = []
    currentTime = CommonsInitValue.initNowTime()

    print '----START CRAW XDNETNEWS OIL NEWS----'
    try:
        XDNetOilNewsSpider.writeMorningOilDailyNews()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'XDNetOilNewsSpider.writeMorningOilDailyNews',e])

    print '----START CRAW YHNET OIL NEWS----'
    try:
        YHNetOilNewsSpider.writeMorningOilDailyNews()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'YHNetOilNewsSpider.writeMorningOilDailyNews',e])


    CommonsRecodeErrorUtils.commonRedcodeError(currentList)