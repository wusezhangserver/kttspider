from themenews_spider import CompanyNewsSpider
from themenews_spider import ImportantNewsSpider
from themenews_spider import ThemeNewsSpider
from themenews_spider import YiCaiCompanyNewsSpider
from themenews_spider import PwThemeNewsSpider
from themenews_spider import CriCompanyNewsSpider
from themenews_spider import StcnThemeNewsSpider
from commonutils_spider import CommonsRecodeErrorUtils
from commonutils_spider import CommonsInitValue
import uuid

def  crawThemeNews():

    currentList = []
    currentTime = CommonsInitValue.initNowTime()

    # CRAW THE IMPORT NEWS
    print '----START CRAW THE IMPORT NEWS----'
    try:
       ImportantNewsSpider.writeCompanyNews()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'ImportantNewsSpider.writeCompanyNews',e])
    
    #CRAW THE COMPANY NEWS
    print '----START CRAW THE COMPANY NEWS----'
    try:
        CompanyNewsSpider.writeCompanyNews()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'CompanyNewsSpider.writeCompanyNews',e])

    #CRAW THE THEME NEWS
    print '----START CRAW THE THEME NEWS----'
    try:
        ThemeNewsSpider.writeThemeDailyNews()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'ThemeNewsSpider.writeThemeDailyNews',e])

    #CRAW THE YICAI NEWS
    print '----START CRAW THE YICAI NEWS----'
    try:
        YiCaiCompanyNewsSpider.writeYiCaiCompanyNews()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'YiCaiCompanyNewsSpider.writeYiCaiCompanyNews',e])

    #CRAW THE PWTHEME NEWS
    print '----START CRAW THE PWTHEME NEWS----'
    try:
        PwThemeNewsSpider.writeDailyThemeNews()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'PwThemeNewsSpider.writeDailyThemeNews',e])

    #CRAW THE CRICOMPANY NEWS
    print '----START CRAW THE CRICOMPANY NEWS----'
    try:
        CriCompanyNewsSpider.writeDailyCompanyNews()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'CriCompanyNewsSpider.writeDailyCompanyNews',e])

    #CRAW THE StcnTheme NEWS
    print '----START CRAW THE StcnTheme NEWS----'
    try:
        StcnThemeNewsSpider.writeDailyThemeNews()
    except Exception, e:
        currentList.append([currentTime,str(uuid.uuid1()),'StcnThemeNewsSpider.writeDailyThemeNews',e])
    CommonsRecodeErrorUtils.commonRedcodeError(currentList)