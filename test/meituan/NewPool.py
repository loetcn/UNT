# -*- coding: UTF-8 –*-

import os,sys
sys.path.append('..')

from meituan import NewTxt
from meituan.public import config
from meituan.public import log

logger = log.logger(__name__ , __file__)

class NewPool(object):

    def __init__(self,FILE, newFile):

        self.Root = "pachong2" #地址
        self.FILE = FILE    # 新建文件地址
        self.newFile = newFile    # 新建文件名称

        #NewTxt.newTxt(self.Root, self.FILE, self.newFile)
        self.newtxt = NewTxt.newTxt(self.Root, self.FILE, self.newFile)     #新建文件返回打开a+模式

    def Circular_Web_Address(self, newWebToFirst, newWebToSecond, first, second):

        """
        根据找到的web爬虫地址，newWebToFirst作为爬虫地址的前半段，newWebToSecond为爬虫地址的后半段，
        pageIndex的初始和结束分别为（first,second）,
        用newtxt写入webAddress的地址。
        """

        for pageIndex in range(int(first), int(second)):
            webAddress = newWebToFirst + str(pageIndex) + newWebToSecond
            self.newtxt.write(webAddress+'\n')
            config.LOG.debug('成功写入第%s条数据，WEB编号为%s', str(pageIndex), str(webAddress))
        self.newtxt.close()

        return
'''
    def split_txt_list(self, FILE):

        """
        获取FILE文件夹中的所有的.txt格式的文件，返回filenamelist。
        """

        import glob
        cwd = os.getcwd()  # 保存当前工作目录
        FILE = str(NewTxt.get_root(self.Root)) +"\\"+ FILE
        if FILE:
            os.chdir(FILE)
        filenamelist = []

        for filename in glob.glob('*.txt'):
            filenamelist.append(str(filename))
        config.LOG.debug('成功获取FILE文件夹里面的txt文件！')
        os.chdir(cwd)
        return filenamelist
'''
'''
    def split_file(self):

        """
        分割newtxt文件，分割成为line_count=30行一个文件？
        """

        try:

            line_count = 30
            temp_count = 0
            temp_content = []
            part_num = 1
            for line in self.newtxt:
                if temp_count < line_count:
                    temp_count += 1
                else:
                    self.write_file(part_num, temp_content)
                    part_num += 1
                    temp_count = 1
                    temp_content = []
                temp_content.append(line)

            else:
                # 正常结束循环后将剩余的内容写入新文件中
                self.write_file(part_num, temp_content)

            config.LOG.debug('成功分割txt文件！')

        except IOError as err:
            config.LOG.error(err)


    def write_file(self, part_num, *line_content):

        """
        将按行分割后的内容写入相应的分割文件中
        """

        part_file_name = NewTxt.newTxt(self.FILE + 'split' , self.newFile+str(part_num))

        try:
            part_file_name.writelines(line_content[0])
            part_file_name.close()
        except IOError as err:
            config.LOG.error(err)

if __name__=="__main__":
    aa = NewPool("Data","ip.txt")
    print(aa.split_txt_list("Data\\iPPool"))
'''