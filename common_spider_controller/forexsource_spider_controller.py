from distutils import log
from forexpic_spider import  CnforexSpider
from forexpic_spider import SwissquoteSpider
def  updateDailyForexPic():
    log.info('The system crawling the resource of forex picture ')
    print '----START CRAW THE FOREX PICTURE----'
    CnforexSpider.findForexImage();
    
    print '----START CRAW THE DAILY NEWS OF FOREX ----'
    log.info('The system crawling the resource of daily news of  forex ')
    SwissquoteSpider.writeSwissquoteTodayNews();
    
if __name__=="__main__":
    updateDailyForexPic()
