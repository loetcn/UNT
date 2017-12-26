# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
def File_data_merging():
#________路径查找_____
    path="E:\\campus big data\\Stat_time\\"
    first_path=open(path+"path_file.txt",'r')
    first_path_read=first_path.read().split('\n')
    for i in range(0,len(first_path_read)):
        print (first_path_read[i],"finish")
        data=first_path_read[i][29:39]   #文档合并使用pandas模块
        a = pd.read_csv("E:\\campus big data\\mingdan.txt",names=['usser','xb','szxy','mz','syd','szbj'],sep="\t")
        #逐块读取文本文件
        b = pd.read_csv(first_path_read[i], names=['usser','time','port'], sep="\t")
        hh=pd.merge(a,b,on='usser')
        #pandas.merge根据一个或多个键将不同的数据集中的行连接起来，以用户进行分类
        txt=hh.to_csv('E:\\campus big data\\File_data_merging\\'+data+'.txt',header=False,index=False,sep='\t')
        #写合并后数据进入txt