# -*- coding: utf-8 -*-
import zipfile
import os
def UNZipfile():
    fr=open("E:\\campus big data\\Datadirectory.txt","r")
    fr_s=fr.read()
    log_files_list =fr_s.split("\n")
    for item in log_files_list:
        #for循环遍历目录
        fi=open(item+'\\zip_file_path.txt','r')
        filename=fi.read().split("\n")
        huafen=(item)[23:34]

        for x in range(0,len(filename)-1):     #遍历目录下的目录
            print (filename[x], "finesh")
            zip_file = zipfile.ZipFile(filename[x])     #解压文件
            for names in zip_file.namelist():
                data=zip_file.read(names)

                fw=open("E:\\campus big data\\data\\"+huafen+"\\"+names,'w')
                fw.write(data)
                fw.close()
            zip_file.close()
    print("ok")