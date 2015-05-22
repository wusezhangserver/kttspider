from distutils import log
from forexpic_spider import CnForexImageSpider
from forexpic_spider import HeXunForexImageSpider
from commonutils_spider import CommonsRecodeErrorUtils
from commonutils_spider import CommonsInitValue
import uuid

def updateDailyForexPic():

    currentList = []
    currentTime = CommonsInitValue.initNowTime()

    log.info('The system crawling the resource of forex picture ')
    print '----START CRAW THE FOREX PICTURE----'
    CnForexImageSpider.writeForexImages()

    print '----START CRAW THE XEHUN PICTURE----'
    try:
        HeXunForexImageSpider.writeHeXunForexImage()
    except Exception,e:
        currentList.append([currentTime,str(uuid.uuid1()),'HeXunForexImageSpider.writeHeXunForexImage',e])

    print '----START CRAW THE DAILY NEWS OF FOREX ----'
    log.info('The system crawling the resource of daily news of  forex ')
    #SwissquoteSpider.writeSwissquoteTodayNews();

    CommonsRecodeErrorUtils.commonRedcodeError(currentList)