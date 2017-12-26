# -*- coding: UTF-8 –*-
import requests
import time
import threadpool
import re
from meituan.NewPool import *
from meituan.Randomer import randomer
import os, sys
sys.path.append('..')

logger = log.logger(__name__ , __file__)

class DetectIP():

    def __init__(self, url,FILE,FILE_Copy):
        #self.FILE = str(NewTxt.get_root("pachong2")) + "\\Data\\iPPool\\" + "ip.txt"
        #self.FILE_Copy = str(NewTxt.get_root("pachong2"))+ "\\Data\\iPPool\\" + url+"\\" +"ip.txt"
        self.FILE = FILE
        self.FILE_Copy =FILE_Copy
        self.proxys = []
        self.start1 = time.time()
        self.url = url
        self.proxysAdd = []
        self.mark = "guess-like"
        return

    def rendProxy(self):
        ippool = open(self.FILE,'r',encoding='utf-8')
        lines = ippool.readlines()
        for i in range(0,len(lines)):
            ip = lines[i].strip("\n").split("\t")
            proxy_host = ip[0]
            proxy_temp = {"http":proxy_host}
            self.proxys.append(proxy_temp)
        ippool.close()

    def myRequest(self,proxy):
        UA = randomer.randomAgentGen()
        headers = {'User-Agent': UA}

        try:
            resp = requests.get(self.url, proxies=proxy, headers=headers,timeout=120)
            config.LOG.debug('成功打开网页' + self.url + "；    发送头文件信息为" + str(headers) + "；    使用ip代理为：" + str(proxy) + "；")
            if resp.status_code ==200:
                if self.mark in resp.text:
                    self.proxysAdd.append(proxy["http"])
                    print(proxy["http"])
                    config.LOG.debug('成功打开网页' + self.url + "代理为："+ proxy["http"]+"；")

        except:
            print("无法访问")

    def timeCost(self):
        print ("Elapsed time: %s" % (time.time()-self.start1))

    def Pooldo(self):
        pool = threadpool.ThreadPool(1000)
        self.rendProxy()
        reqs = threadpool.makeRequests(self.myRequest, self.proxys)
        [pool.putRequest(req) for req in reqs]
        pool.wait()
        ippools = open(self.FILE_Copy, "w")
        for nub in range(0, len(self.proxysAdd)):
            ippools.writelines(self.proxysAdd[nub] + '\n')
        ippools.close()
        self.timeCost()

url ="http://i.meituan.com"
num = re.sub("[http://]", "", url)
print(num)

FILE = str(NewTxt.get_root("pachong2")) + "\\Data\\iPPool\\" + "ip.txt"
FILE_Copy = str(NewTxt.get_root("pachong2"))+ "\\Data\\iPPool\\" +num+ "_ip.txt"
a = DetectIP(url,FILE,FILE_Copy)
a.Pooldo()
