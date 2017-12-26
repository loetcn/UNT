import time
import requests
import threadpool
import re

wechat = []

f = open("wechatNub.txt")
lines = f.readlines()

for i in range(0,len(lines)):
    ip = lines[i].strip("\n").split("\t")
    wechatNub = ip[0]
    url = "http://weixin.sogou.com/weixin?type=1&query=" + wechatNub + "&ie=utf8&_sug_=n&_sug_type_="
    wechat.append(url)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}

ipPool =[]
Regular ='</script><div target="_blank" href="(.*?)"'

def myRequest(url):

    try:
        resp = requests.get(url,headers=headers,timeout=60)
        print(url, str(resp.status_code))
        xx = resp.text
        if 'results mt7' in xx:
            pattern = re.compile(Regular, re.S)
            items = re.findall(pattern, xx)
            item = str(items[0]).replace("amp;","")

            print(item)
            ipPool.append(item)
    except:
        print(url)


def timeCost():
    print ("Elapsed time: %s" % (time.time()-start1))

start1 = time.time()
pool = threadpool.ThreadPool(1000)
reqs = threadpool.makeRequests(myRequest, wechat)
[ pool.putRequest(req) for req in reqs ]
pool.wait()

with open("ippppp.txt", "a") as f:
    for x in range(0, len(ipPool)):
        f.writelines(str(ipPool[x]) + '\n')

timeCost()


