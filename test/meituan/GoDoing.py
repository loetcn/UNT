# -*- coding: UTF-8 –*-
from meituan.BusinessInfor import BusinessUp
from meituan import NewTxt
from meituan.public import config
from meituan.public import log
from meituan.TimeDoer import TimeDoer


import time
import re
import os, sys

sys.path.append('..')

logger = log.logger(__name__ , __file__)

url ="http://i.meituan.com"
num = re.sub("[http://]", "", url)

FILE = str(NewTxt.get_root("pachong2")) + "\\Data\\iPPool\\" + "ip.txt"
FILE_Copy = str(NewTxt.get_root("pachong2"))+ "\\Data\\iPPool\\" +"weixinurl" + "_ip.txt"
while 1:
    time.sleep(TimeDoer.doFirst(14,45,00))
    buS = BusinessUp.BusinessUp()   # 下载大理地区信息。
    buS.BusinessDo()
