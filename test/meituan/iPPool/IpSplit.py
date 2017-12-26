# -*- coding: UTF-8 –*-

import requests
import pickle
import threadpool
import time
import re
from meituan.NewPool import *
from selenium.common.exceptions import StaleElementReferenceException
from meituan.public import config
from meituan.public import log
from meituan.Randomer import randomer
import os, sys
sys.path.append('..')

logger = log.logger(__name__ , __file__)

class IpSqlit():

    def __init__(self):
        self.FILE = "FILE"

        self.iPOpener = NewPool("Data\\ippool", 'ipp.txt').newtxt
        self.FILE = str(NewTxt.get_root("pachong2")) + "\\Data\\iPPool\\" + "www.xicidaili.comnn_ip.txt"
        self.url = "http://www.xicidaili.com/nn/"
        self.weblen = 1300
        self.start1 = time.time()
        return

    def waitForLoad(self, driver):
        elem = driver.find_element_by_tag_name("html")
        count = 0
        while True:
            count += 1
            if count > 20:
                print("Timing out after 10 seconds and returning")
                return
            time.sleep(.5)
            try:
                elem == driver.find_element_by_tag_name("html")
            except StaleElementReferenceException:
                return

    def BuildPool(self):

        return

    def myRequest(self, url, temp_count):

        headers = self.headersOpen(temp_count)
        proxys =self.proxyOpener(temp_count)
        contents = []
        try:
            resp = requests.get(url, headers=headers, proxies=proxys, timeout=60)
            config.LOG.debug('成功打开网页' + url + "；    发送头文件信息为" + str(headers) + "；    使用ip代理为：" + str(proxys) + "；")
            config.LOG.debug("打开网页" + url + "   返回HTTP状态码为：" +str(resp.status_code))
            print(url, str(resp.status_code))
            ss = resp.text
            r_txt = re.compile(
                '<td>(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])</td>.*?<td>(\d{2,4})</td>',
                re.S)
            items = re.findall(r_txt, str(ss))

            for nub in range(0, len(items)):
                content = '%s.%s.%s.%s:%s' % tuple(items[nub])
                contents.append(content)
            print(contents)

            for nub in range(0, len(contents)):
                self.iPOpener.writelines(contents[nub] + '\n')
            time.sleep(5)

            return

        except :
            config.LOG.error("网页发生错误"+ url + "  " + str(headers) + "     " + str(proxys))

    def headersOpen(self,temp_count):

        headers_count = 100
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

        proxy_count = 200
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

        for nub in range(1, self.weblen):
            urladd = self.url + str(nub)
            urls.append(urladd)

        for nub in range(1, self.weblen):
            nubs.append(nub)

        for i in zip(urls, nubs):
            func = (list(i), None)
            func_var.append(func)

        return func_var

    def timeCost(self):
        print("Elapsed time: %s" % (time.time() - self.start1))
"""
    def ipDo(self):
        pool = threadpool.ThreadPool(50)
        reqs = threadpool.makeRequests(self.myRequest, self.func_var())
        [pool.putRequest(req) for req in reqs]
        for nub in range(1, len(self.contents)):
            self.iPOpener.writelines(self.contents[nub] + '\n')
        pool.wait()
        self.iPOpener.close()
        self.timeCost()

"""
if __name__=="__main__":

    aa = IpSqlit()
    pool = threadpool.ThreadPool(50)
    reqs = threadpool.makeRequests(aa.myRequest, aa.func_var())
    [pool.putRequest(req) for req in reqs]
    pool.wait()
    aa.iPOpener.close()
    aa.timeCost()
