# -*- coding: utf-8 -*-
import os
import time
from collections import Counter
import copy

def time_port_stat(dir_prefix):  #
    new_dir_prefix = dir_prefix.replace("New_data", "Stat_time")
    total_info = new_dir_prefix + dir_prefix.rsplit('\\', 2)[1] + "Ch_student.txt"
    result = new_dir_prefix + dir_prefix.rsplit('\\', 2)[1] + "Ch_student1.txt"
    file_dir = new_dir_prefix + "Ch_students\\"

    filename = [fname for fname in os.listdir(file_dir) if fname.endswith('.txt')]
    fw = open(total_info, 'w')
    for e in filename:
        file_path = file_dir + e
        fread = open(file_path, 'r')
        content = fread.read()
        fread.close()
        fw.write(content)
    fw.close()
    fread = open(total_info, 'r')
    fread_txt = fread.read()
    txt_list = fread_txt.split('\n')
    txt_list.pop()
    fread.close()
    for i in range(len(txt_list)):
        txt_list[i] = txt_list[i].split("\t")

    txt_sorted = sorted(txt_list, key=lambda x: x[0])
    del (txt_list)
    users_lists = []  # "去重之前的用户列表

    for i in range(len(txt_sorted)):
        users_lists.append(txt_sorted[i][0])
    statis_info = []
    users_list = list(set(users_lists))
    users_list.sort()
    result = new_dir_prefix + dir_prefix.rsplit('\\', 2)[1] + "_" + str(len(users_list)) + "_Ch_student.txt"
    fw = open(result, "w")
    for account in users_list:
        time_temp = []
        port_dict = {}
        tag = 0  # 每个账号第一次出现用tag=1表示,不匹配用tag=0表示
        try:
            for item in txt_sorted:
                if tag == 0 and len(port_dict) > 0:
                    break
                if item[0] == account:
                    tag = 1
                    t1 = (item[1])[0:5]
                    t2 = (item[2])[0:5]
                    dict1 = eval("{" + item[3] + "}")
                    time_temp.append(t1)
                    time_temp.append(t2)
                    port_dict = dict(Counter(port_dict) + Counter(dict1))
                else:
                    tag = 0
        except:
            print( item)
        time_list = sorted(list(set(time_temp)))
        time_temp = copy.copy(time_list)

        i = 1
        j = 1
        while i < len(time_temp) - 1:
            if (time_temp[i + 1])[0:2] == (time_temp[i])[0:2]:
                if int((time_temp[i + 1])[3:5]) - int((time_temp[i])[3:5]) < 40:
                    del time_list[j]
                    i = i + 1
                else:
                    j = j + 2
                    i = i + 2
            else:
                if int((time_temp[i + 1])[3:5]) + 60 - int((time_temp[i])[3:5]) < 10:
                    del time_list[j]
                    i = i + 1
                else:
                    j = j + 2
                    i = i + 2

        each_row = account + '\t' + str(time_list) + "\t" + str(port_dict) + "\n"
        #      print each_row
        fw.write(each_row)
        del each_row
        del time_list
        del time_temp
        del port_dict
    fw.close()


def travel(filename):
    fread_directory = open(filename, 'r')
    floders_path = fread_directory.read().split('\n')
    floders_path.pop()
    fread_directory.close()
    for path_prefix in floders_path:
        start = time.clock()
        time_port_stat(path_prefix)
        end = time.clock()
        print(path_prefix, " finished!   The running time is :", (end - start) / 60, "minutes!")


data_path = "D:\\campus big data\\New_Datadirectory.txt"
travel(data_path)