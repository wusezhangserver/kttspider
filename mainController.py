from common_spider_controller import morningnews_spider_controller
from common_spider_controller import headline_spider_controller
from common_spider_controller import dailyblog_spider_controller
from common_spider_controller import dailytheme_spider_controller
from common_spider_controller import forexpic_spider_controller
from common_spider_controller import dailycomment_spider_controller
from apscheduler.schedulers.blocking import BlockingScheduler

def crawdailynews():
    print '********************************start spider  morningnews********************'
    morningnews_spider_controller.crawDailyNews()

def crawdatacenter():
    print '********************************start spider headlingnews********************'
    headline_spider_controller.crawDataCenter()

def updateblogdata():
    print '********************************start spider dailyblog************************'
    dailyblog_spider_controller.updateBlogData()

def crawthemenews():
    print '********************************start spider dailytheme***********************'
    dailytheme_spider_controller.crawThemeNews()

def updatedailyforexpic():
    print '********************************start spider forexpic************************'
    forexpic_spider_controller.updateDailyForexPic()

def crawcommentsnews():
    print '********************************start spider commentsnews************************'
    dailycomment_spider_controller.crawCommentsNews()

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(crawdailynews, 'interval', seconds=3600)
    scheduler.add_job(crawdatacenter,'interval',secondds=3600)
    scheduler.add_job(updateblogdata,'interval',secondds=3600)
    scheduler.add_job(crawthemenews,'interval',secondds=3600)
    scheduler.add_job(updatedailyforexpic,'interval',secondds=3600)
    scheduler.add_job(crawcommentsnews,'interval',secondds=3600)
    print('*************system spiders init now ***********')

    try:
        scheduler.start()
        print ('*******start craw information*******')
    except (KeyboardInterrupt, SystemExit):
        pass