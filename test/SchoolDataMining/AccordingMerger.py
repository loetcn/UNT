# -*- coding: utf-8 -*-
import os
#统计每天上网人数
def day_internet_people():
    path="E:\\campus big data\\"
    first_path=open(path+"New_Datadirectory.txt",'r')
    first_path_read=first_path.read().split('\n')
    print (first_path_read)
    for i in range(0,len(first_path_read)-1):
        try:
            txt_file=[fname for fname in os.listdir(first_path_read[i]) if fname.endswith('_Ch_student.txt')]
            all_path=first_path_read[i]+txt_file[0]       #完整路径的合成
            print (all_path)
            newlist=(all_path.split("\\",3)[3])[22:26]     #截取路径中的人数部分
            data=(all_path.split("\\",3)[3])[5:10]
            print (newlist)
            swrs=data+"\t"+newlist
            gg=[swrs]
            print (gg)
            fw=open("E:\\campus big data\\shujixueyuan\\"+"all_school_day_people_number.xls",'a')
            for e in gg:
                fw.write(e)
                fw.write('\n')
            fw.close()
        except:
            pass