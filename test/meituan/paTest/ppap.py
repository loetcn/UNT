import time
import re
import threadpool
import requests
from selenium.common.exceptions import StaleElementReferenceException

def waitForLoad(driver):
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

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
f = open("ip.txt", 'a')
contents = []
def myRequest(url):
    resp = requests.get(url, headers=headers)
    try:

            print(url, str(resp.status_code))
            ss = resp.text
            r_txt = re.compile(
                '<td>(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])</td>.*?<td>(\d{2,4})</td>',
                re.S)
            items = re.findall(r_txt, str(ss))

            for nub in range(1, len(items)):
                content = '%s.%s.%s.%s:%s' %  tuple(items[nub])
                contents.append(content)

            time.sleep(50)
            return

    except ConnectionError:

        print("无法访问")
        print(ConnectionError)

def timeCost():
    print ("Elapsed time: %s" % (time.time()-start1))


urls = []
url = "http://www.xicidaili.com/nn/"
for nub in range(1,1130):

    urladd = url +str(nub)
    urls.append(urladd)

start1 = time.time()
pool = threadpool.ThreadPool(10)
reqs = threadpool.makeRequests(myRequest, urls)
[ pool.putRequest(req) for req in reqs ]

for nub in range(1, len(contents)):
    f.writelines(contents[nub] + '\n')
f.close()
pool.wait()
timeCost()

