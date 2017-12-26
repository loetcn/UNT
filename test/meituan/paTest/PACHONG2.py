import time
import requests
import threadpool
import httplib2

proxys = []
#http = httplib2.Http()

f = open("ip.txt")
lines = f.readlines()

for i in range(0,len(lines)):
    ip = lines[i].strip("\n").split("\t")
    proxy_host = ip[0]
    proxy_temp = {"http": proxy_host}
    proxys.append(proxy_temp)

"""
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
url = 'http://i.meituan.com/deal/details/7057504'
resp = requests.get(url,headers=headers)
line =resp.text

if "套餐内容" in line:
    print(line)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}

ipPool =[]
url = "http://mp.weixin.qq.com/profile?src=3&timestamp=1479544928&ver=1&signature=bSQwGNXezYizejeUiVAJL5g8rIoOp5yjHIbWGfV1*qIAb4UAsHj6dZTplRrE35Fa0MnFrXsVDs2KcB8bE4zcRw=="
def myRequest(proxy):
    resp = requests.get(url, headers=headers, proxies=proxy, timeout=60)
    try:
        #http.request(url, headers=headers)
        #f =open("pacxx.txt",'a')
        #f.write(str(resp.text.encode("utf-8")))
        #f.write("\n")
        #f.write("***************************************************************************************")
        #f.close()
        print(proxy, str(resp.status_code))
        xx = resp.text
        if '和讯外汇' in xx:
            ipPool.append(proxy)
    except:
        print(proxy)


def timeCost():
    print ("Elapsed time: %s" % (time.time()-start1))

start1 = time.time()
pool = threadpool.ThreadPool(1000)
reqs = threadpool.makeRequests(myRequest, proxys)
[ pool.putRequest(req) for req in reqs ]
pool.wait()

with open("xxx111111.txt", "a") as f:
    for x in range(1, len(ipPool)):
        f.writelines(str(ipPool[x]) + '\n')

timeCost()


