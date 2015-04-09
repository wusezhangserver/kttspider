from common_spider_controller import morningnews_spider_controller
from common_spider_controller import headline_spider_controller


if __name__ == '__main__':
   print '********************************start spider  morningnews********************'
   morningnews_spider_controller.crawDailyNews()
   print '********************************start spider headlingnews********************'
   headline_spider_controller.crawDataCenter()