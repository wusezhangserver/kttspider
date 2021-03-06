
import urllib

    
def  openUrl(webHttp):
    urlopen  = urllib.urlopen(webHttp) 
    context = urlopen.read()
    urlopen.close()
    return  context

def filterContextBy(context,filter):
    return context.find(filter)

def filterContextByTarget(context,startfilter,endfilter):
    return context[filterContextBy(context,startfilter)+len(startfilter):filterContextBy(context,endfilter)]

def filterSwissQuoteImage(link):
    context = openUrl(link)
    filterContext = context[filterContextBy(context,'<div class="contentArticle ">'):]
    imagelink = filterContextByTarget(filterContextByTarget(filterContext,'<div class="contentArticle ">','</img>'),'src=','width')
    imageurl = imagelink[1:len(imagelink)-4]
    return imageurl

def writeSwissQuoteImage(imageurl):
    urllib.urlretrieve(imageurl, imageurl[len('http://files.ac-markets.com/Newsletter/0000-00-00/'):])
    
if __name__ == '__main__':
    link = 'http://cn.swissquote.com/fx/news/daily-fx-news/2014/4/25'
    filterSwissQuoteImage(link)
       
    
    
    