# -*- coding: UTF-8 –*-

import requests
import pickle
import threadpool
import time
import re
from meituan.NewPool import *
from meituan.public import config
from meituan.public import log
from meituan.Randomer import randomer
import os, sys
sys.path.append('..')

logger = log.logger(__name__ , __file__)

class BusinessComment():

    def __init__(self):
        self.FILE = "FILE"
        self.localtime = time.strftime("%Y%m%d%H%M%S")
        self.FILE = str(NewTxt.get_root("pachong2")) + "\\Data\\iPPool\\" + "i.meiuan.comdali_ip.txt"
        self.FILEBUSI = str(NewTxt.get_root("pachong2")) + "\\Data\\business\\" + "business_infor.txt"
        self.weblen = 310
        self.start1 = time.time()
        return

    def OpenRead(self):
        return

    def myRequest(self, url, address):
        iPOpener = NewPool("Data\\business", 'business_' + address + '_infor').newtxt
        n = 1
        while 1:
            contents = []
            headers = self.headersOpen(n)
            proxys = self.proxyOpener(n)
            urler = url + str(n)
            resp = requests.get(urler, timeout=60,headers=headers, proxies=proxys)
            ss = resp.text
            if 'user-wrapper' in ss:
                r_txt = re.compile(
                    r'<weak class="username">(.*?)</weak>.*?<span class="stars">(.*?)</span>.*?<weak class="time">(.*?)</weak>.*?<p>(.*?)</p>',
                    re.S)
                items = re.findall(r_txt, ss)
                print(urler + "  成功！")
                for nub in range(0, len(items)):
                    xx = list(items[nub])
                    x = xx[1]
                    numb = x.count('<i class="text-icon icon-star">')
                    xx[1] = numb
                    dr = re.compile(r'<[^>]+>', re.S)
                    xx[3] = dr.sub('', xx[3]).strip()
                    content = '%s   %s   %s   %s' % tuple(xx)
                    contents.append(content)
                for nub in range(0, len(contents)):
                    iPOpener.write(+contents[nub]+"\n")
                print(contents)
                n += 1
            else:
                print(urler + "  error")
                iPOpener.close()
                break

            """
            try:
                resp = requests.get(urler, headers=headers, proxies=proxys, timeout=60)
                config.LOG.debug('成功打开网页' + urler + "；    发送头文件信息为" + str(headers) + "；    使用ip代理为：" + str(proxys) + "；")
                config.LOG.debug("打开网页" + urler + "   返回HTTP状态码为：" +str(resp.status_code))
                ss = resp.text
                if 'user-wrapper' in ss:
                    r_txt = re.compile(
                        r'<weak class="username">(.*?)</weak>.*?<span class="stars">(.*?)</span>.*?<weak class="time">(.*?)</weak>.*?<p>(.*?)</p>',
                        re.S)
                    items = re.findall(r_txt, ss)
                    print(urler+ "  成功！")
                    for nub in range(0, len(items)):
                        xx = list(items[nub])
                        x = xx[1]
                        numb = x.count('<i class="text-icon icon-star">')
                        xx[1] = numb
                        dr = re.compile(r'<[^>]+>', re.S)
                        xx[3] = dr.sub('', xx[3]).strip()
                        content = '%s   %s   %s   %s' % tuple(xx)
                        contents.append(content)

                    for nub in range(0, len(contents)):
                        iPOpener.write(address+ "   " +contents[nub]+"\n")

                    time.sleep(5)

                else:
                    print(urler + "  error")
                    break

            except :
                print(urler +"    error")
                config.LOG.error("网页发生错误"+ urler + "  " + str(headers) + "     " + str(proxys))
            """


    def headersOpen(self,temp_count):

        headers_count = 10
        part_count = 1

        try:
            if temp_count % headers_count == 0:
                UA = randomer.randomAgentGen()
                headers = {'User-Agent': UA}
                pickle.dump(headers, open('tmp.txt', 'wb'))

                return headers

            elif part_count % temp_count ==0:
                UA = randomer.randomAgentGen()
                headers = {'User-Agent': UA}
                pickle.dump(headers, open('tmp.txt', 'wb'))

            else:
                getback = pickle.load(open('tmp.txt', 'rb'))
                return getback

        except :

            UA = randomer.randomAgentGen()
            headers = {'User-Agent': UA}
            return headers


    def proxyOpener(self,temp_count):

        proxy_count = 5
        part_count = 1

        try :
            if temp_count % proxy_count == 0:
                Ip = randomer.randomIpproxy(self.FILE)
                proxy ={"http":Ip}
                pickle.dump(proxy, open('ipproxy.txt', 'wb'))

                return proxy

            elif part_count % temp_count == 1:
                Ip = randomer.randomIpproxy(self.FILE)
                proxy = {"http": Ip}
                pickle.dump(proxy, open('ipproxy.txt', 'wb'))
                return proxy


            else:
                getback = pickle.load(open('ipproxy.txt', 'rb'))
                return getback

        except IOError:
            Ip = randomer.randomIpproxy(self.FILE)
            proxy = {"http": Ip}
            return proxy

    def func_var(self):

        urls = []
        nubs = []
        func_var = []
        lines = open(self.FILEBUSI).readlines()
        for i in range(0, len(lines)):
            BusinessU = lines[i].strip("\n").split("   ")
            address= BusinessU[0]
            url = "http://i.meituan.com/deal/" + address + "/feedback/page_"
            urls.append(url)

        for nub in range(0, len(lines)):
            BusinessU = lines[nub].strip("\n").split("   ")
            address= BusinessU[0]
            nubs.append(address)

        for i in zip(urls, nubs):
            func = (list(i), None)
            func_var.append(func)

        return func_var

    def timeCost(self):
        print("Elapsed time: %s" % (time.time() - self.start1))

    def BusinessDo(self):
        pool = threadpool.ThreadPool(1)
        reqs = threadpool.makeRequests(self.myRequest, self.func_var())
        [pool.putRequest(req) for req in reqs]

        pool.wait()
        self.timeCost()


if __name__=="__main__":
    aa =BusinessComment()
    aa.BusinessDo()
