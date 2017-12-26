# -*- coding: utf-8 -*-
import os
import time
#[用户名，时间区间列表，端口列表]
def time_port_stat(dir_prefix):   #定义一个函数
    file_dir=dir_prefix +"china students\\"
    txt_filename=[fname for fname in os.listdir(file_dir) if fname.endswith('.txt')]#搜索指定目录下txt文
    for e in txt_filename:
        file_path=file_dir+e
        fread=open(file_path,'r')             #打开txt文档
        fread_txt=fread.read()               #读取txt文档
        fread.close()
        txt_list=fread_txt.split('\n')
        txt_list.pop()
        for i in range(len(txt_list)):
            txt_list[i]=txt_list[i].split("\t")
        txt_sorted=sorted(txt_list,key=lambda x:x[1])#数据排序
        del(txt_list)   #删除原数据
        users_lists=[]  #"去重之前的用户列表
        for i in range(len(txt_sorted)):
            users_lists.append(txt_sorted[i][1])   #把内容加到列表里面
        statis_info = []
        users_list=list(set(users_lists))
        users_list.sort()
        fw=open(result , "w")
        for account in users_list:
            each_user=[]
            time_temp=[]
            time_list=[]
            port_list=[]
            port_dic={}
            tag=0    #每个账号第一次出现用tag=1表示,不匹配用tag=0表示
            for item in txt_sorted:
                if tag==0 and len(port_list)>0:
                    break
                if item[1]==account:
                    tag=1
                    time_temp.append(item[0])
                    port_list.append(item[6])
                else:
                    tag=0
            time_list.append(min(time_temp))
            time_list.append(max(time_temp))
            port_norepeat=list(set(port_list))
            for e in port_norepeat:
                port_dic[e]=port_list.count(e)
                each_row=account+'\t'+(time_list[0])[15:22]+"\t"+(time_list[1])[15:22]+"\t"+str(port_dic)[1:len(str(port_dic))-1]+"\n"
            fw.write(each_row)
            del each_row
            del time_temp
            del time_list
            del port_list
            del port_norepeat
            del port_dic
            del each_user
        fw.close()
def travel(filename):
    fread_directory=open(filename,'r')
    floders_path=fread_directory.read().split('\n')
    floders_path.pop()
    for path_prefix in floders_path:
        time_port_stat(path_prefix)
        print(path_prefix," fineshed")
