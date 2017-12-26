import requests
import time
import threadpool

urls = []

f = open("ip.txt")
lines = f.readlines()

for i in range(0,len(lines)):
    ip = lines[i].strip("\n").split("\t")
    url = ip[0]
    urls.append(url)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
ipPool = []
def myRequest(url):

    try:
        resp = requests.get(url,headers=headers,timeout=60)
        print(url, str(resp.status_code))
        xx = resp.text
        if 'container' in xx:
            ipPool.append(url)
    except:
        print(url)


def timeCost():
    print ("Elapsed time: %s" % (time.time()-start1))

start1 = time.time()
pool = threadpool.ThreadPool(1000)
reqs = threadpool.makeRequests(myRequest, urls)
[ pool.putRequest(req) for req in reqs ]
pool.wait()

with open("xxx111111.txt", "a") as f:
    for x in range(1, len(ipPool)):
        f.writelines(str(ipPool[x]) + '\n')

timeCost()
