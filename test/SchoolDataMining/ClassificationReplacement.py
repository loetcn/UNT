# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np

def File_data_merging():
    # 路径查找
    path = "E:\\campus big data\\File_data_merging\\file_path.txt"
    first_path = open(path, 'r')
    first_path_read = first_path.read().split('\n')
    for i in range(0, len(first_path_read)):
        print
        first_path_read[i], "finish"
        data = first_path_read[i][37:47]
        # print data
        # 文档合并使用pandas模块
        a = pd.read_csv("E:\\campus big data\\jidian.txt", names=['usser', 'jd'], sep="\t")  # 逐块读取文本文件
        b = pd.read_csv(first_path_read[i], names=['usser', 'xb', 'szxy', 'mz', 'syd', 'szbj', 'time', 'port'],
                        sep="\t")
        hh = pd.merge(a, b, on='usser')  # pandas.merge根据一个或多个键将不同的数据集中的行连接起来，以用户进行分类
        # print b
        print
        len(hh)
        txt = hh.to_csv('E:\\campus big data\\File_data_merging\\later_data_merging\\' + data + '.txt', header=False,
                        index=False, sep='\t')  # 写合并后数据进入txt


def statistics_of_population():
    path = "E:\\campus big data\\File_data_merging\\later_data_merging\\"
    txt_file = [fname for fname in os.listdir(path) if fname.endswith('.txt')]
    for j in range(0, len(txt_file)):
        file_path = path + txt_file[j]
        print
        file_path, "finish!"
        two_path = open(file_path, 'r')
        two_path_read = two_path.read().split('\n')
        file_name = (file_path.split("\\", 5)[4])[0:10]
        # print file_name
        for k in range(0, len(two_path_read) - 1):
            time_qujian = two_path_read[k].split("\t")
            time = eval(time_qujian[7])
            # print time
            list1 = []
            for p in range(0, len(time)):
                time_int = int((time[p])[0:2])  # 将数据转化成整形
                # print time_int
                list1.append(time_int)
            # print list1
            star_list = []
            stop_list = []
            for item in range(0, len(list1)):
                if item % 2 != 0:
                    star = list1[item - 1]
                    stop = list1[item]
                    star_list.append(star)
                    stop_list.append(stop)
            time_duan = list(map(lambda x: x[0] - x[1], zip(stop_list,
                                                            star_list)))  # 实现两个列表相减 (zip函数接受任意多个序列作为参数，返回一个元组列表l=[11, 21]，k=[14, 23]，zip(k,l)=[(14,11),(23,21)]
            # lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x[0]-x[1]为函数体
            # map第一个参数接收一个函数名，第二个参数接收一个可迭代对象
            long_time = sum(time_duan)  # 列表求和
            # print long_time
            rr = two_path_read[k] + '\t' + str(long_time)
            # print rr
            qq = rr.split('\t')
            jidian = eval(qq[1])
            '''if jidian==0:
                qq[1]='D' '''
            if 0 <= jidian < 2:
                qq[1] = 'C'
            if 2 <= jidian < 3:
                qq[1] = 'B'
            if 3 <= jidian <= 4:
                qq[1] = 'A'
            zongji_time = int(qq[9])
            if 0 <= zongji_time <= 3:
                qq[9] = '0-3'
            if 3 < zongji_time < 8:
                qq[9] = '4-8'
            if 8 <= zongji_time <= 12:
                qq[9] = '8-12'
            if 12 < zongji_time <= 24:
                qq[9] = '13-24'
            ww = qq[0] + '\t' + qq[1] + '\t' + qq[2] + '\t' + qq[3] + '\t' + qq[4] + '\t' + qq[5] + '\t' + qq[
                6] + '\t' + qq[9] + '\t' + qq[8]

            # print ww
            fw = open("E:\\campus big data\\File_data_merging\\new_data\\" + file_name + '.txt', 'a')
            fw.write(ww + '\n')
            fw.close()