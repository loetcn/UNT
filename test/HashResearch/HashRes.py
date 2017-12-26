# -*- coding: utf-8 -*-
import imagehash
from PIL import Image
import pandas as pd
import time

"""
    使用imagehash的包，里面包含了所有的哈希图像相似度算法；
    使用PIL（Pillow）图像包，内置图片处理的各种方法和函数；
    使用pandas 包，通过pandas进行csv文件数据处理；
    使用time包，通过time.clock()函数进行时间记录。
"""

def hamming_distance( string1, string2):
    '''
    See: http://en.wikipedia.org/wiki/Hamming_distance
    汉明距离（hamming_distance）函数  它表示两个(相同长度)字对应位不同的数量，我们以d(x,y)表示两个字x,y之间的汉明距离。
    对两个字符串进行异或运算，并统计结果为1的个数，那么这个数就是汉明距离。
    注：zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    '''

    diffs = 0
    for c1, c2 in zip(string1, string2):
        if c1 != c2:
            diffs += 1
    return diffs

def is_similar( image_path1, image_path2, n):
    '''
    比较相似度（is_similar）函数  它将两照片的hash值求出汉明距离（hamming_distance）值，再转换为百分数。
    :param image_path1:
    :param image_path2:
    :param n:
    :return:
    '''
    distance = hamming_distance(list(str(image_path1)), list(str(image_path2)))
    value = float(100 - ((100 / n) * distance))
    return value

def dohash( phth1 , phth2 , n):
    '''
    比较哈希（dohash）函数  比较两张照片的aHash、pHash和dHash的哈希值，通过使用imagehash.phash()和imagehash.average_hash()，
    以及imagehash.dhash()，可以得出照片phash、ahash、dhash的具体数值，再使用比较相似度（is_similar）函数求出相似度。
    注：phth1、phth2 为照片的绝对路径，哈希函数需要使用PIL进行打开照片才能进行哈希数值计算。其中，n参数为选择照片的压缩尺寸。
    :param phth1:
    :param phth2:
    :param n:
    :return:
    '''
    photo_path_one = Image.open(phth1)
    photo_path_two = Image.open(phth2)
    phashs1 = imagehash.phash(photo_path_one, hash_size=n)
    phashs2 = imagehash.phash(photo_path_two, hash_size=n)
    ahashs1 = imagehash.average_hash(photo_path_one, hash_size=n)
    ahashs2 = imagehash.average_hash(photo_path_two, hash_size=n)
    dhashs1 = imagehash.dhash(photo_path_one, hash_size=n)
    dhashs2 = imagehash.dhash(photo_path_two, hash_size=n)

    true_value_p = is_similar(phashs1, phashs2, 2 * n)
    true_value_a = is_similar(ahashs1, ahashs2, 2 * n)
    true_value_d = is_similar(dhashs1, dhashs2, 2 * n)

    return true_value_a,true_value_p,true_value_d

def readcsv(imgpath ,csvpath, n):
    '''
    随机选择照片（readcsv）函数  使用pandas读取csvpath（即存放所有的'CaptureEventID'的CSV文件），使用pandas的随机选取样本函数
    DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
    进行对'CaptureEventID'的选取，而n为需要选取的个数。并且使用读取照片路径（readpath）函数进行对照片路径进行读取
    （其中：imgpath 参数为照片路径存放的CSV文件）。再使用列表的[].append()函数进行保存再列表中。
    :param imgpath:
    :param csvpath:
    :param n:
    :return:
    '''
    x = []
    df = pd.read_csv(csvpath)
    while len(x) < n:
        ds = df.sample(n=1)
        a = list(ds['CaptureEventID'].as_matrix())
        try:
            ls = readpath(imgpath, a, n=3)
            if ls != False:
                x.append(ls)
        except:
            print("chucuo")
    print(len(x))
    print(x)

    return x

def readpath( imgpath, a, n):
    '''
    读取照片路径（readpath）函数  imgpath 参数为照片路径存放的CSV文件，a参数为读入的列表（其中存放'CaptureEventID'，
    通过这个进行选择照片），n为选择后的照片路径的个数。
    首先，使用pandas读取csv文件，然后使用DataFrame.loc()函数通过行标签索引行数据进行选择，
    选择其中的'(df["CaptureEventID"] == a[0])'的ds行数据，再判断ds的行数是否为n行（已经规定n=3），
    如是进行list()，DataFrame转为列表。return该列表。
    :param imgpath:
    :param a:
    :param n:
    :return:
    '''
    df = pd.read_csv(imgpath)
    ds = df.loc[(df["CaptureEventID"] == a[0])]
    if len(ds) == n:
        ix = list(ds['URL_Info'].as_matrix())
        print(ix)
        return ix
    else:
        return False

def dotimeAhash(ls, a, n ):
    '''
    计算Ahash运行时间（dotimeAhash）函数  ls参数为所有的照片路径存放的列表。
    a参数为每组照片的个数(已经规定为a=3)，n参数为选择照片的压缩尺寸。
    bengin = time.clock()和end = time.clock()用来计时。
    余下的两个函数dotimeDhash()、dotimePhash()相同。
    :param ls:
    :param a:
    :param n:
    :return:
    '''
    if a == 3:
        bengin = time.clock()
        for ix in ls:
            for i in range(0,a):
                if a <= i+1:
                    photo_path_one = Image.open(ix[i])
                    photo_path_two = Image.open(ix[i+1])
                    ahashs1 = imagehash.average_hash(photo_path_one, hash_size=n)
                    ahashs2 = imagehash.average_hash(photo_path_two, hash_size=n)
                    is_similar(ahashs1, ahashs2, 2 * n)
        end = time.clock()
        timelet =end - bengin
        return timelet

def dotimeDhash(ls, a, n ):
    '''
    计算Dhash运行时间（dotimeDhash）函数  与计算Ahash运行时间（dotimeAhash）函数 相同。
    :param ls:
    :param a:
    :param n:
    :return:
    '''

    if a == 3:
        bengin = time.clock()
        for ix in ls:
            for i in range(0,a):
                if a <= i+1:
                    photo_path_one = Image.open(ix[i])
                    photo_path_two = Image.open(ix[i+1])
                    dhashs1 = imagehash.dhash(photo_path_one, hash_size=n)
                    dhashs2 = imagehash.dhash(photo_path_two, hash_size=n)
                    is_similar(dhashs1, dhashs2, 2 * n)
        end = time.clock()
        timelet =end - bengin
        return timelet

def dotimePhash(ls, a, n ):
    '''
    计算Phash运行时间（dotimePhash）函数  与计算Ahash运行时间（dotimeAhash）函数 相同。
    :param ls:
    :param a:
    :param n:
    :return:
    '''
    if a == 3:
        bengin = time.clock()
        for ix in ls:
            for i in range(0,a):
                if a <= i+1:
                    photo_path_one = Image.open(ix[i])
                    photo_path_two = Image.open(ix[i+1])
                    phashs1 = imagehash.phash(photo_path_one, hash_size=n)
                    phashs2 = imagehash.phash(photo_path_two, hash_size=n)
                    is_similar(phashs1, phashs2, 2 * n)
        end = time.clock()
        timelet =end - bengin
        return timelet
