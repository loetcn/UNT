import requests
from meituan.NewPool import *
import threadpool
from meituan.public import config
from meituan.public import log
from meituan.Randomer.randomer import randomAgentGen
import os, sys
sys.path.append('..')
logger = log.logger(__name__ , __file__)
import collections




def myRequest( url,temp_count):

    headers = headersOpen(temp_count)
    resp = requests.get(url, headers=headers)
    print(headers)
    print(url)
    proxys = "1.60.14.225:8888"
    # resp = requests.get(url, headers=headers, proxies=proxys)
    print(resp.status_code)

def headersOpen(temp_count):
    headers_count = 10
    part_num = 1
    headers = ""
    if temp_count % headers_count ==0:
        UA = randomAgentGen()
        headers = {'User-Agent': UA}
        part_num += 1
    return headers

"""
while 1:
    myRequest("https://www.baidu.com")
"""
f = open("ip.txt", 'a')

urls = []
nubs =[]
func_var =[]

url = "http://www.xicidaili.com/nn/"
contents = []
for nub in range(1, 100):
    urladd = url + str(nub)
    urls.append(urladd)

for nub in range(1,100):
    nubs.append(nub)

for i in zip(urls,nubs):
    # print(list(i))
    func = (list(i) ,None)
    # print(func)
    func_var.append(func)
# print(func_var)

pool = threadpool.ThreadPool(2)

reqs = threadpool.makeRequests(myRequest, func_var)
[pool.putRequest(req) for req in reqs]

pool.wait()

f.close()