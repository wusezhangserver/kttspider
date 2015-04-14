from distutils import log
from forexpic_spider import  CnForexImageSpider

def  updateDailyForexPic():

    log.info('The system crawling the resource of forex picture ')
    print '----START CRAW THE FOREX PICTURE----'
    CnForexImageSpider.findForexImage();
    
    print '----START CRAW THE DAILY NEWS OF FOREX ----'
    log.info('The system crawling the resource of daily news of  forex ')
    #SwissquoteSpider.writeSwissquoteTodayNews();
