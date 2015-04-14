from common_spider_controller import morningnews_spider_controller
from common_spider_controller import headline_spider_controller
from common_spider_controller import dailyblog_spider_controller
from common_spider_controller import dailytheme_spider_controller
from common_spider_controller import forexpic_spider_controller

if __name__ == '__main__':
   print '********************************start spider  morningnews********************'
   morningnews_spider_controller.crawDailyNews()
   print '********************************start spider headlingnews********************'
   headline_spider_controller.crawDataCenter()
   print '********************************start spider dailyblog************************'
   dailyblog_spider_controller.updateBlogData()
   print '********************************start spider dailytheme***********************'
   dailytheme_spider_controller.crawThemeNews()
   print '********************************start spider forexpic************************'
   forexpic_spider_controller.updateDailyForexPic()