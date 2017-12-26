# -*- coding:utf-8 -*-
import os
from PIL import Image
import time
import re
import imghdr

def IsChackInfo( pathfile):
    try:
        img = Image.open(pathfile)
        exif_data = img._getexif()
        try:

            exif_time = exif_data[36868]
            time_exif = re.findall(r"[\w']+", exif_time)
            a = str(time_exif[0]) + "-" + str(time_exif[1]) + "-" + str(time_exif[2]) + " " + str(time_exif[3]) + ":" + \
                str(time_exif[4]) + ":" +str(time_exif[5])
            timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
            timeStamp = int(time.mktime(timeArray))
            img.close()

            return timeStamp
        except:
            img.close()
            return False
    except:
        return False

def makeList(S_dir):

    func_var =[]
    func_var_to =[]
    for filename in os.listdir(S_dir):
        if imghdr.what(S_dir+"\\"+filename):
            infodi = IsChackInfo(S_dir+"\\"+filename)
            if infodi != False:
                func = (filename, infodi )
                func_var.append(func)

    func_var.sort(key=lambda x: x[1])
    n = 0
    m = 1
    while n < len(func_var)-1:

        if abs(func_var[n+1][1] - func_var[n][1]) <= 90:
            func_next = (func_var[n][0], func_var[n][1],m)
            func_var_to.append(func_next)
            n = n + 1
        else:
            func_next = (func_var[n][0], func_var[n][1],m)
            func_var_to.append(func_next)
            n = n + 1
            m = m + 1
    del func_var
    return func_var_to

def writerList(C_dir,func):

    with open(C_dir+'\\'+'egg2.csv', 'w') as csvfile:
        csvfile.write("photoname,timestamp,grouping\n")
        for func_list in func:
            csvfile.write(str(func_list[0])+","+str(func_list[1])+","+str(func_list[2])+"\n")
        csvfile.close()

def main(s_dir,c_dir):

    fun = makeList(s_dir)
    writerList(c_dir,fun)
    del fun

