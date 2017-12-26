# -*- coding: utf-8 -*-
import os

def Datadirectory():
    data_file_path="E:\\campus big data\\Data\\"
    log_file_path=os.listdir(data_file_path)
    log_files_list =[]
    fw=open("E:\\campus big data\\Datadirectory.txt",'w')
    for i in log_file_path:
        fw.write(data_file_path+i  +"\\")
        fw.write("\n")
    fw.close()

def CreateLogDirectory():
    fr=open("E:\\campus big data\\Datadirectory.txt","r")
    fr_s=fr.read()
    log_files_list=fr_s.split("\n")
    for item in log_files_list:
        fw=open(item+"file_path.txt","w")
        try:
            log_filename=[fname for fname in os.listdir(item) if fname.endswith('.log')]
            for fname in log_filename:
                fw.write(item+fname)
                fw.write("\n")
        except:
            pass
        fw.close()
    fr.close()