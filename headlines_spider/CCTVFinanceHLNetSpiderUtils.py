from commonutils_spider import CommonsSpiderUtils
from commonutils_spider import CommonsMysqlUtils

def returnStartContext(link,startTarget):
    return CommonsSpiderUtils.returnSpecialStartContext(link,startTarget)

def filterContextByTarget(context,startfilter,endfilter):
    return CommonsSpiderUtils.filterContextByTarget(context,startfilter,endfilter)

def findAllTarget(context,filterTarget):
    return CommonsSpiderUtils.findAllTargets(context,filterTarget) 

def removeSpecialCharacter(removeContext):
    return CommonsSpiderUtils.removeSpecialCharacter(removeContext)

def divisionTarget(startcontext,startfilter,endfilter):
    return CommonsSpiderUtils.divisionTarget(startcontext,startfilter,endfilter)

def filterAfterContext(startContext,filterContext):
    return startContext[CommonsSpiderUtils.filterContext(startContext,filterContext)+len(filterContext):]

# GET MYSQL CONNECTION
def getMySQLConn():
    return CommonsMysqlUtils.returnMySQLConn()