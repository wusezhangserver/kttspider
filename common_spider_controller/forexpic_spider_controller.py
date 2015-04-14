from distutils import log
from forexpic_spider import CnForexImageSpider
from forexpic_spider import HeXunForexImageSpider

def updateDailyForexPic():

    log.info('The system crawling the resource of forex picture ')
    print '----START CRAW THE FOREX PICTURE----'
    CnForexImageSpider.writeForexImages()

    print '----START CRAW THE XEHUN PICTURE----'
    HeXunForexImageSpider.writeHeXunForexImage()

    print '----START CRAW THE DAILY NEWS OF FOREX ----'
    log.info('The system crawling the resource of daily news of  forex ')
    #SwissquoteSpider.writeSwissquoteTodayNews();
