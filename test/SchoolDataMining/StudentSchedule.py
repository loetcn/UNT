# -*- coding: utf-8 -*-
import os
# 统计8-10,10-12,12-14,14-16,16-19,19-21,21-0,0-7,7—8每个时段间用校园网的人数,假设8-10,10-12,12-14,14-16,16-19,19-21,21-0,0-7,7-8分别是t1,t2,t3,t4,t5,t6,t7,t8，t9
def statistics_of_population():
    path = "E:\\campus big data\\"
    first_path = open(path + "New_Datadirectory.txt", 'r')
    first_path_read = first_path.read().split('\n')
    # print first_path_read

    for i in range(0, len(first_path_read) - 1):
        try:
            txt_file = [fname for fname in os.listdir(first_path_read[i]) if fname.endswith('_Ch_student.txt')]
            file_path = first_path_read[i] + txt_file[0]
            print(file_path, "finish")
        except:
            pass
        for i in range(0, len(file_path) - 1):
            two_path = open(file_path, 'r')
            two_path_read = two_path.read().split('\n')
            file_name = file_path.split("\\", 4)[3]
            # print file_name
            # print two_path_read
            t1 = 0
            t2 = 0
            t3 = 0
            t4 = 0
            t5 = 0
            t6 = 0
            t7 = 0
            t8 = 0
            t9 = 0
            # -------------------读取时间并将整数部分提取，使之存入列表
            for j in range(0, len(two_path_read) - 1):
                time_data = two_path_read[j].split("\t")
                time_qujian = eval(time_data[1])  # eval（）将字符串str当成有效表达式并返回计算结果
                print(time_qujian)
                list1 = []  # 创建一个存储数据的新列表
                for time in range(0, len(time_qujian)):
                    time_int = int((time_qujian[time])[0:2])  # 将数据转化成整形
                    list1.append(time_int)
                print(list1)
                # ——————————————----------------填充区间内的数字———————————
                for item in range(0, len(list1)):
                    if item % 2 != 0:
                        star = list1[item - 1]
                        stop = list1[item]
                        list2 = range(star, stop + 1)
                        # print list2


                        list3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
                        list4 = list(set(list2) & set(list3))  # 求并集
                        # print list4
                        # ——按条件进行筛选和计数每一时段上网的人数————
                        gg = [x for x in list4 if 8 <= x < 10]  # 判断所生成的列表中元素是否满足条件，满足条件的自动生成一个新列表
                        if len(gg) > 0:
                            t1 += 1
                        # print  't1=', t1
                        tt = [x for x in list4 if 10 <= x < 12]  # 列表推导式
                        if len(tt) > 0:
                            t2 = t2 + 1
                        nn = [x for x in list4 if 12 <= x < 14]
                        if len(nn) > 0:
                            t3 = t3 + 1
                        # print  't3=', t3
                        ff = [x for x in list4 if 14 <= x < 16]
                        if len(ff) > 0:
                            t4 = t4 + 1
                        # print  't4=', t4
                        aa = [x for x in list4 if 16 <= x < 19]
                        if len(aa) > 0:
                            t5 = t5 + 1
                        # print  't5=', t5
                        bb = [x for x in list4 if 19 <= x < 21]
                        if len(bb) > 0:
                            t6 = t6 + 1
                            # print  't6=', t6
                        cc = [x for x in list4 if 21 <= x <= 23]
                        if len(cc) > 0:
                            t7 = t7 + 1
                        # print  't7=', t7

                        dd = [x for x in list4 if 0 <= x <= 6]
                        if len(dd) > 0:
                            t8 = t8 + 1
                        # print  't8=', t8
                        ff = [x for x in list4 if 6 <= x < 8]
                        if len(ff) > 0:
                            t9 = t9 + 1
                            # print  't9=', t9
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------将统计好的数据写入excel中-----------------------------------------------
            fw = open("E:\\campus big data\\result\\" + "qujian_people_number.xls", 'a')
            fw.write(file_name + "\t" + str(t1) + '\t' + str(t2) + '\t' + str(t3) + '\t' + str(t4) + '\t' + str(t5) + '\t' + str(
                t6) + '\t' + str(t7) + '\t' + str(t8) + '\t' + str(t9) + '\n')
            fw.write('\n')
            fw.close()


def Number_of_people_playing_games():
    path = "E:\\campus big data\\File_data_merging\\"
    first_path = open(path + "file_path.txt", 'r')
    first_path_read = first_path.read().split('\n')  # 读取路径

    for i in range(0, len(first_path_read) - 1):
        print(first_path_read[i], "finish")
        data = first_path_read[i][37:47]
        two_path_fr = open(first_path_read[i], 'r')
        two_path_read = two_path_fr.read().split('\n')
        # print (two_path_read)
        t = 0
        for k in range(0, len(two_path_read) - 1):
            port_qujian = two_path_read[k].split("\t")
            port = eval(port_qujian[7])
            # print (port)
            port_tiqu = port.keys()  # 提取字典中的键
            # print (port_tiqu)
            yx = [5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010, 5011, 5012, 5013, 5014, 5015, 5016,
                  5017, 5018, 5019, 5020, 5021, 5022, 5023, 5024, 5025, 5026, 5027, 5028, 5029, 5030, 5031, 5032, 5033,
                  5034, 5035, 5036, 5037, 5038, 5039, 5040, 5041, 5042, 5043, 5044]  # 游戏端口
            cont = False
            for item in port_tiqu:
                if int(item) in yx:  # 判断日志文件中的端口是否在游戏端口里
                    cont = True
                    t += 1
                    break  # 如果有一个存在就马上跳出循环
                    # print str(t)
        fw = open("E:\\campus big data\\result\\Number_of_people_playing_games1.xls", 'a')
        fw.write(data + '\t' + str(t))
        fw.write('\n')
        fw.close()