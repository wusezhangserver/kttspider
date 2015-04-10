import time
import datetime

def initTempImage():
    return 'http://216.189.56.159/imagelib/iconresource/editor/2x_web/ic_insert_invitation_grey600_36dp.png'

def initNowTime():
    return  time.strftime("%Y-%m-%d %X",time.localtime())

def initBeforeDayTime():
    now_time = datetime.datetime.now()
    befor_time = now_time + datetime.timedelta(days=-1)
    yes_time_format =  befor_time.strftime('%Y-%m-%d')
    return yes_time_format