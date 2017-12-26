
from meituan.public import config
from meituan.public import log
from meituan.Randomer import randomer


logger = log.logger(__name__ , __file__)

def headersOpen():

    headers_count = 300
    part_num = 1
    headers = ""
    for temp_count in range(1,901):
        if temp_count % headers_count != 0:
            temp_count += 1
            print(temp_count)
        else:
            headers = randomer.randomAgentGen()
            print(headers)
            print(temp_count)
            part_num += 1
            temp_count = 1
            temp_content = []

    return headers

headersOpen()