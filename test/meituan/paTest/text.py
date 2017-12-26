import requests
import re

"""
n = 1
while 1:
    contents = []
    url = "http://i.meituan.com/deal/37419702/feedback/page_"
    urler = url + str(n)
    resp = requests.get(urler, timeout=60)
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
        print(contents)
        n += 1
    else:
        print(urler +"  error")

        continue
"""

'''
def myRequest():

    url ="http://i.meituan.com/dali?p="
    headers ={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0',}
    n= 246

    f = open("xx.txt", "a+",encoding="utf-8")
    while 1:
        contents = []
        urler ="http://i.meituan.com/s/dali-麦辣鸡翅（2块）+小可乐1份"

        resp = requests.get(urler,headers=headers, timeout=60)
        ss = resp.text
        if "list list-in" in ss:
            print(urler + "   " + str(resp.status_code))
            r_txt = re.compile(
                '<div class="title text-block">(.*?)</div>.*?<del>(.*?)元</del>',
                re.S)
            items = re.findall(r_txt, str(ss))

            for nub in range(0, len(items)):
                xx = list(items[nub])
                dr = re.compile(r'<[^>]+>', re.S)
                xx[0] = dr.sub('', xx[0]).replace("\n", "")
                print(xx)
                content = '%s %s' % tuple(xx)
                contents.append(content)
            print(contents)

            for nub in range(0, len(contents)):
                f.write(contents[nub]+"\n")
            n += 1
            resp.close()
            break
        elif "no-deals" in ss:
            print(urler + "   暂无此类团购，请查看其他分类")
            resp.close()
            f.close()
            break
        elif "btn-wrapper" in ss:
            print(urler + "   验证码！")
            resp.close()
            f.close()
            break
        else:
            print(urler + "   不知名error?")
            resp.close()

myRequest()
'''
import time
from meituan import NewTxt
from meituan.public import config
from meituan.public import log
import os, sys
from meituan.BloomFilterMan import bloomfilterOnRedis
sys.path.append('..')

logger = log.logger(__name__ , __file__)
Cm ="Data\\business"
KNOWNDO = NewTxt.split_txt_list(Cm)
print(KNOWNDO)


for x in range(0,2):
    opener = bloomfilterOnRedis.BloomFilter
    opener().openServer()
    bf = bloomfilterOnRedis.BloomFilter()
    f = open(str(NewTxt.get_root("pachong2")) +"\\"+ Cm+"\\"+str(KNOWNDO[x]), "r",encoding="utf-8")
    lines = f.readlines()
    proxys = []
    proxy = []
    for i in range(0, len(lines)):
        ip = lines[i].strip("\n").split("\t")
        proxys.append(ip)
    f.close()
    u = open(str(NewTxt.get_root("pachong2")) +"\\"+ Cm+"\\"+KNOWNDO[x], "w+", encoding="gbk")
    for ix in range(0, len(proxys)):
        ip = proxys[ix]
        if bf.isContains(ip):
            continue
        else:
            bf.insert(ip)
            u.write(str(ip[0]) + "\n")

    u.close()
    time.sleep(5)
    opener().closeServer()
