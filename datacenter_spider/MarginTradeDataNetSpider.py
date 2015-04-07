from  selenium import webdriver
import sys
sys.path.append("../commonutils_spider/")
import CommonsMysqlUtils


def crawMarginTradeDataSource(link,keylist):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainContext = browsor.find_element_by_id('grid-1-TS').text.split('\n')
    for var in mainContext:
        varList = var.split(' ')
        if not (varList[0] in keylist):
            varList[1]=varList[1].replace(',','')
            varList[2]=varList[2].replace(',','')
            varList[3]=varList[3].replace(',','')
            varList[4]=varList[4].replace(',','')
            varList[5]=varList[5].replace(',','')
            varList[6]=varList[6].replace(',','')
            varList = varList[0:7]
            currentArray.append(varList)
    return currentArray
    
def writeMarginTradeDataSource():
    link = 'http://stock.jrj.com.cn/rzrq/jyzs.shtml'
    dbManager = CommonsMysqlUtils._dbManager
    selectSQL = " SELECT  SUBSTRING(RESOURCE.JYRQ,1,10) AS JYRQ " \
                " FROM  DATACENTER_MARGINTRADE_RESOURCE_TABLE RESOURCE WHERE 1=1 "
    selectDict =dbManager.selectDictMany(selectSQL)
    keyList = []
    for current_dict in selectDict:
            for (key,value) in current_dict.iteritems():
                keyList.append(value)

    currentArray = crawMarginTradeDataSource(link,keyList)
    SQL = ' INSERT INTO DATACENTER_MARGINTRADE_RESOURCE_TABLE (JYRQ,RZMRE,RZYE,RQMCL,RQYL,RQYE,RZRQYE)' \
          ' VALUES(%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(SQL,currentArray)