# -*- coding: utf-8 -*-
import os
def MultilevelDirectory():
    fr = open("E:\\campus big data\\Datadirectory.txt", 'r')
    fr_read = fr.read()
    log_files_list = fr_read.split("\n")
    for i in log_files_list:
        path = i
        new_path = os.path.join(i, 'china students')  # join(path,*paths)连接两个或多个路径
        if not os.path.isdir(new_path):  # 判断path是否为目录
            os.makedirs(new_path)  # 创建目录本国学生
        new_path = os.path.join(i, 'foreign students')

        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        new_path = os.path.join(i, 'teacher')

        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        new_path = os.path.join(i, 'youth hostel')
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        fr.close()