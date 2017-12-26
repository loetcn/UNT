# -*- coding: UTF-8 –*-

import os, sys
from meituan.public import config
from meituan.public import log
sys.path.append('..')

logger = log.logger(__name__ , __file__)

def get_root(root):

    """
    查看root是否为当前的文档下面，是就返回
    """
    path = os.getcwd()

    while root != os.path.basename(path):
        path = os.path.dirname(path)
    return path

def newTxt(Root, FILE , newFile):

    """
    新建文件夹在FILE中，newFile为新建的txt名字。
    并且返回txtPath的读写行为。
    """
    ROOT = get_root(Root)
    try:
        os.mkdir( os.path.join(ROOT, FILE))
        config.LOG.debug('新建文件夹'+ FILE +'成功！')
        txtPath = open(FILE + '\\' + newFile + '.txt', 'a+')
        config.LOG.debug('新建'+ newFile +'TXT文件成功！')
        return txtPath

    except OSError as err :
        txtPath = open(ROOT+"\\"+FILE + '\\' + newFile + '.txt', 'a+',encoding='utf-8')
        config.LOG.error(err)
        config.LOG.debug('打开'+ newFile +'TXT文件成功！')

        return txtPath

    except:
        txtPath = open(ROOT+"\\"+FILE + '\\' + newFile + '.txt', 'a+',encoding='utf-8')
        config.LOG.error("不知道名错误")
        config.LOG.debug('打开'+ newFile +'TXT文件成功！')

        return txtPath

def split_txt_list( FILE):

    """
    获取FILE文件夹中的所有的.txt格式的文件，返回filenamelist。
    """

    import glob
    cwd = os.getcwd()  # 保存当前工作目录
    FILE = str(get_root("pachong2")) +"\\"+ FILE
    if FILE:
        os.chdir(FILE)
    filenamelist = []

    for filename in glob.glob('*.txt'):
        filenamelist.append(str(filename))
    config.LOG.debug('成功获取FILE文件夹里面的txt文件！')
    os.chdir(cwd)
    return filenamelist
