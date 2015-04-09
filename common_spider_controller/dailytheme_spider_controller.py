from themenews_spider import CompanyNewsSpider
from themenews_spider import ImportantNewsSpider
from themenews_spider import ThemeNewsSpider
from themenews_spider import YiCaiCompanyNewsSpider
from themenews_spider import PwThemeNewsSpider
from themenews_spider import CriCompanyNewsSpider
from themenews_spider import StcnThemeNewsSpider


def  crawThemeNews():
    # CRAW THE IMPORT NEWS
    print '----START CRAW THE IMPORT NEWS----'
    ImportantNewsSpider.writeCompanyNews()
    
    #CRAW THE COMPANY NEWS
    print '----START CRAW THE COMPANY NEWS----'
    CompanyNewsSpider.writeCompanyNews()
    
    #CRAW THE THEME NEWS
    print '----START CRAW THE THEME NEWS----'
    ThemeNewsSpider.writeThemeDailyNews()
    
    #CRAW THE YICAI NEWS
    print '----START CRAW THE YICAI NEWS----'
    YiCaiCompanyNewsSpider.writeYiCaiCompanyNews()
    
    #CRAW THE PWTHEME NEWS
    print '----START CRAW THE PWTHEME NEWS----'
    PwThemeNewsSpider.writeDailyThemeNews()
    
    #CRAW THE CRICOMPANY NEWS
    print '----START CRAW THE CRICOMPANY NEWS----'
    CriCompanyNewsSpider.writeDailyCompanyNews()
    
    #CRAW THE StcnTheme NEWS
    print '----START CRAW THE StcnTheme NEWS----'
    StcnThemeNewsSpider.writeDailyThemeNews()