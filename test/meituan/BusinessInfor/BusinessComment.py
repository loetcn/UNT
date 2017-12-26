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
        self.address ="dali"
        self.localtime = time.strftime("%Y%m%d%H%M%S")
        self.FILE = str(NewTxt.get_root("pachong2")) + "\\Data\\iPPool\\" + "i.meiuan.comdali_ip.txt"
        self.FILEBUSI = str(NewTxt.get_root("pachong2")) + "\\Data\\business_infor\\" + "business_"+self.address+"_infor.txt"
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
            #proxys ={"http":""}
            urler = url + str(n)
            try:
                n = self.deepdo(n, urler, contents, iPOpener)
                if n ==0:
                    break

            except EnvironmentError as er:
                print(urler, er, "  失败！??!!!!!?")
                n = self.deepdo(n, urler, contents, iPOpener)
                if n ==0:
                    break

            except:
                print(urler,  "  失败?")
                n = self.deepdo(n, urler, contents, iPOpener)
                if n ==0:
                    break

        iPOpener.close()
    def deepdo(self, n, urler, contents, iPOpener):

        try:
            headers = self.headersOpen(n)
            proxys = self.proxyOpener(n)
            resp = requests.get(urler, timeout=60, headers=headers, proxies=proxys)
            config.LOG.debug('成功打开网页' + urler + "；    发送头文件信息为" + str(headers) + "；    使用ip代理为：" + str(proxys) + "；")
            config.LOG.debug("打开网页" + urler + "   返回HTTP状态码为：" + str(resp.status_code))
            ss = resp.text
            if 'user-wrapper' in ss:
                r_txt = re.compile(
                    r'<weak class="username">(.*?)</weak>.*?<span class="stars">(.*?)</span>.*?<weak class="time">(.*?)</weak>.*?<p>(.*?)</p>',
                    re.S)
                items = re.findall(r_txt, ss)

                for nub in range(0, len(items)):
                    xx = list(items[nub])
                    x = xx[1]
                    numb = x.count('<i class="text-icon icon-star">')
                    xx[1] = numb
                    dr = re.compile(r'<[^>]+>', re.S)

                    xx[3] = dr.sub('', xx[3].replace("\n", "")).strip()
                    content = '%s   %s   %s   %s' % tuple(xx)
                    contents.append(content)
                for nub in range(0, len(contents)):
                    iPOpener.write(contents[nub] + "\n")

                resp.close()
                print(urler + "  成功！")
                n += 1

            elif "btn-wrapper" in ss:
                print(urler + "  失败！","输入验证码！")
                self.deepdo(n, urler, contents, iPOpener)

            else:
                resp.close()
                n = 0

            return n

        except EnvironmentError as er:
            print(urler ,er,"  失败！???")
            self.deepdo(n, urler, contents, iPOpener)

        except requests.exceptions.ProxyError:
            print(requests.exceptions.ProxyError)
            self.deepdo(n, urler, contents, iPOpener)
        except :
            print("eeeeeeeeeeeeeee")
            self.deepdo(n, urler, contents, iPOpener)

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

        except EOFError:
            Ip = randomer.randomIpproxy(self.FILE)
            proxy = {"http": Ip}
            return proxy
        except:
            Ip = randomer.randomIpproxy(self.FILE)
            proxy = {"http": Ip}
            return proxy

    def func_var(self):

        urls = []
        nubs = []
        func_var = []
        lines = open(self.FILEBUSI,"r",encoding="UTF-8").readlines()
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
        pool = threadpool.ThreadPool(10)
        reqs = threadpool.makeRequests(self.myRequest, self.func_var())
        [pool.putRequest(req) for req in reqs]

        pool.wait()
        self.timeCost()

'''
if __name__=="__main__":
    aa =BusinessComment()
    aa.BusinessDo()
'''