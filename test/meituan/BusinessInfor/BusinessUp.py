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

class BusinessUp():

    def __init__(self):
        self.FILE = "FILE"
        self.address= "dali"
        self.localtime = time.strftime("%Y%m%d%H")
        self.FILE = str(NewTxt.get_root("pachong2")) + "\\Data\\iPPool\\" + "i.meiuan.comdali_ip.txt"
        self.url = "http://i.meituan.com/"+self.address+"?p="
        self.weblen = 310
        self.start1 = time.time()


    def myRequest(self, url, temp_count):
        iPOpener = NewPool("Data\\business_infor", 'business_' + self.address + "_" + self.localtime + '_infor').newtxt
        contents = []
        headers = self.headersOpen(temp_count)
        #proxys =self.proxyOpener(temp_count)
        proxys = {"http": ""}

        try:
            resp = requests.get(url, headers=headers, proxies=proxys, timeout=10)
            config.LOG.debug('成功打开网页' + url + "；    发送头文件信息为" + str(headers) + "；    使用ip代理为：" + str(proxys) + "；")
            config.LOG.debug("打开网页" + url + "   返回HTTP状态码为：" + str(resp.status_code))
            ss = resp.text
            if resp.status_code == 200:
                if "list list-in" in ss:
                    print(url + "   "+str(resp.status_code))
                    r_txt = re.compile(
                        'data-did="(.*?)">.*?<div class="dealcard-brand single-line">(.*?)</div>.*?<div class="title text-block">(.*?)</div>.*?<span class="strong">(.*?)</span>.*?<del>(.*?)元</del>.*?<span class="line-right">\n\t                    已售(.*?)\n\t            </span>',
                        re.S)
                    items = re.findall(r_txt, str(ss))
                    for nub in range(0, len(items)):
                        xx = list(items[nub])
                        dr = re.compile(r'<[^>]+>', re.S)
                        xx[2] = dr.sub('', xx[2]).replace("\n", "")
                        content = '%s   %s   %s   %s   %s   %s' % tuple(xx)
                        contents.append(content)

                    for nub in range(0, len(contents)):
                        iPOpener.write(contents[nub]+"\n")

                    resp.close()

                elif "no-deals" in ss:
                    print(url + "   暂无此类团购，请查看其他分类")
                    resp.close()

                elif "btn-wrapper" in ss:
                    print(url + "   验证码！")
                    resp.close()
                    self.myRequest(url,100)
                else:
                    print(url + "   不知名错误！")
                    open("www.txt","w",encoding="utf-8").write(ss)
                    resp.close()
                    self.myRequest(url,100)

            else:
                print(url +" ?"+str(resp.status_code))
                resp.close()
                self.myRequest(url, temp_count)

        except EnvironmentError as er:
            print(er, "网页无法打开！")
            self.myRequest(url, temp_count)
            config.LOG.error(er, "网页发生错误" + url + "  " + str(headers) + "     " + str(proxys))

        iPOpener.close()
        time.sleep(5)

    def headersOpen(self,temp_count):

        headers_count = 1000
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

        proxy_count = 10
        part_count = 1

        try:

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

    def BusinessDo(self):
        pool = threadpool.ThreadPool(100)
        reqs = threadpool.makeRequests(self.myRequest, self.func_var())
        [pool.putRequest(req) for req in reqs]
        pool.wait()
        self.timeCost()

if __name__=="__main__":
    aa =BusinessUp()
    aa.BusinessDo()
