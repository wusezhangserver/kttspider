import time
import datetime
import re

def initTempImage():
    return 'http://216.189.56.159/imagelib/initsource/initimage.png'

def initoiltempimage():
    return 'http://216.189.56.159/imagelib/initsource/oiltemp.jpg'

def initNowTime():
    return  time.strftime("%Y-%m-%d %X",time.localtime())

def initBeforeDayTime():
    now_time = datetime.datetime.now()
    befor_time = now_time + datetime.timedelta(days=-1)
    yes_time_format =  befor_time.strftime('%Y-%m-%d')
    return yes_time_format

def returnCreateDate(text):
    currentYear = str(time.strftime('%Y',time.localtime(time.time())))
    group = re.findall(r'[\d|.]+',text)
    if len(group[0])<2:
        group[0] ='0'+ group[0]
    if len(group[1])<2:
        group[1] ='0'+ group[1]
    return currentYear+'-'+ group[0]+'-'+group[1]

def splitCreateDate(text,target,returnnum):
    listContext = text.split(target)
    return listContext[returnnum]

def removeSpecialCharacter(removeContext):
    return removeContext.replace('\n','').replace(' ','').replace('<br>','').replace('<p>','').replace('</p>','').replace('<br/>','')
