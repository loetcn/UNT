#coding=utf-8
import os

def File_data_merging():#创建所有数据合并成一个txt文档函数
#_路径查找_
    path="E:\\campus big data\\File_data_merging\\new_data\\"
    txt_file=[fname for fname in os.listdir(path) if fname.endswith('.txt')]
    for j in range(0,len(txt_file)):
        file_path=path+txt_file[j]
        print (file_path,"finish!")
        fo = open("E:\\campus big data\\File_data_merging\\new_data\\hb.txt", 'a')
        fi = open(file_path)
        while True:
            s = fi.read(16*1024)
            if not s:
                break
            fo.write(s)
        fi.close()
        fo.close()
def dataset():
    path="E:\\campus big data\\File_data_merging\\new_data\\hb.txt"
    two_path=open(path,'r')
    two_path_read=two_path.read().split('\n')
    for k in range(0,len(two_path_read)-1):
        ziduan=two_path_read[k].split("\t")
        #print ziduan
        zuhe1=str(ziduan[1]+'\t'+ziduan[7])+'\n'    #绩点和上网时长数据集
        zuhe2=str(ziduan[3]+'\t'+ziduan[7])+'\n'    #学院和上网时长数据集
        zuhe3=str(ziduan[2]+'\t'+ziduan[7])+'\n'    #性别和上网时长数据集
        zuhe4=str(ziduan[5]+'\t'+ziduan[7])+'\n'    #生源地和上网时长数据集
        zuhe5=str(ziduan[1]+'\t'+ziduan[5])+'\n'    #绩点和生源地数据集
        zuhe6=str(ziduan[3]+'\t'+ziduan[1])+'\n'    #学院和绩点数据集
        zuhe7=str(ziduan[7]+'\t'+ziduan[5]+'\t'+ziduan[1])+'\n'   #上网时长、生源地、绩点
        zuhe8=str(ziduan[7]+'\t'+ziduan[6]+'\t'+ziduan[1])+'\n'   #上网时长、专业、绩点数据集
        zuhe9=str(ziduan[6]+'\t'+ziduan[1])+'\n'    #专业和绩点数据集
        #print zuhe9
        fw=open("E:\\campus big data\\File_data_merging\\dataset\\jd_and_sc.txt",'a')
        fw.write(zuhe1)
        fw=open("E:\\campus big data\\File_data_merging\\dataset\\xy-and_sc.txt",'a')
        fw.write(zuhe2)
        fw=open("E:\\campus big data\\File_data_merging\\dataset\\xb-and_sc.txt",'a')
        fw.write(zuhe3)
        fw=open("E:\\campus big data\\File_data_merging\\dataset\\syd-and_sc.txt",'a')
        fw.write(zuhe4)
        fw=open("E:\\campus big data\\File_data_merging\\dataset\\jd-and_syd.txt",'a')
        fw.write(zuhe5)
        fw=open("E:\\campus big data\\File_data_merging\\dataset\\xy-and_jd.txt",'a')
        fw.write(zuhe6)
        fw=open("E:\\campus big data\\File_data_merging\\dataset\\sc_syd_jd.txt",'a')
        fw.write(zuhe7)
        fw=open("E:\\campus big data\\File_data_merging\\dataset\\sc-zy_jd.txt",'a')
        fw.write(zuhe8)
        fw=open("E:\\campus big data\\File_data_merging\\dataset\\zy-and_jd.txt",'a')
        fw.write(zuhe9)
#File_data_merging()

# --------------------------------用Apriori算法来发现频繁集---------------------
def loadDataSet():  # 读取数据集的函数
    fr = open("E:\\campus big data\\File_data_merging\\dataset\\zuhe2\\2016-03-02.txt", "r")
    data = fr.read().split("\n")
    fr.close()
    dataSet = []  # 存储需挖掘关联规则的数据集的列表
    for i in range(0, len(data)):
        data_text = data[i].split("\t")
        dataSet.append(data_text)
    print(dataSet)
    return dataSet
def createC1(dataSet):
    C1 = []  # C1即为元素个数为1的项集
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)

def scanD(D, Ck, minSupport):  # minSupport为设定的最小支持度
    ssCnt = {}

    for tid in D:  # D为全部数据集
        for can in Ck:  # Ck为大小为k（包含k个元素）的候选项集
            if can.issubset(tid):
                ssCnt[can] = ssCnt.get(can, 0) + 1
                numItems = float(len(D))
                retList = []
                supportData = {}
                for key in ssCnt:
                    support = ssCnt[key] / numItems
                    if support >= minSupport:
                        retList.insert(0, key)
                    supportData[key] = support
                return retList, supportData  # retList为在Ck中找出的频繁项集（支持度大于minSupport的），supportData记录各频繁项集的支持度

def aprioriGen(Lk, k):  # 该函数通过频繁项集列表Lk和项集个数k生成候选项集Ck+1
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k - 2]
            L2 = list(Lk[j])[:k - 2]  # 前k-2项相同时，将两个集合合并
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList

def apriori(dataSet, minSupport=0.5):
    C1 = createC1(dataSet)  # C1通过createC1()函数生成
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2], k)  # Ck表示项数为k的候选项集
        Lk, supK = scanD(D, Ck, minSupport)  # Lk表示项数为k的频繁项集,
        supportData.update(supK)  # supK为其支持度
        L.append(Lk)  # Lk和supK由scanD()函数通过Ck计算而来
        k += 1
    return L, supportData  # L和supportData为所有的频繁项集及其支持度

# -----------------------------从频繁集中挖掘相关规则---------------------------
def generateRules(L, supportData, minConf=0.7):  # 频繁项集列表L，最小可信度阈值minConf
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:  # freqSet为当前遍历的频繁项集
            H1 = [frozenset([item]) for item in freqSet]
            rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)

    return bigRuleList  # 包含可信度的规则列表bigRuleList


def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    # 对候选规则集进行评估
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            print(freqSet - conseq, '-->', conseq, 'conf:', conf)
            brl.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
            return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    while (len(freqSet) > m):  # 判断长度 > m，这时即可求H的可信度
        H = calcConf(freqSet, H, supportData, brl, minConf)
        if (len(H) > 1):  # 判断求完可信度后是否还有可信度大于阈值的项用来生成下一层H
            H = aprioriGen(H, m + 1)
            m += 1
        else:  # 不能继续生成下一层候选关联规则，提前退出循环
            break