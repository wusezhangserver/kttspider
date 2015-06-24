from common_spider_controller import morningnews_spider_controller
from common_spider_controller import headline_spider_controller
from common_spider_controller import dailyblog_spider_controller
from common_spider_controller import dailytheme_spider_controller
from common_spider_controller import forexpic_spider_controller
from common_spider_controller import dailycomment_spider_controller
from common_spider_controller import morningoil_spider_controller

def crawdailynews():
    print '********************************start spider  morningnews********************'
    morningnews_spider_controller.crawDailyNews()

def crawDailyOilNews():
    print '********************************start spider  morningoilnews********************'
    morningoil_spider_controller.crawDailyOilNews()

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
    crawdailynews()
    crawDailyOilNews()
    crawdatacenter()
    updateblogdata()
    crawthemenews()
    updatedailyforexpic()
    crawcommentsnews()
