#!/usr/bin/python
# -*- coding:gb2312 -*-

import os, sys
import logging

def get_root(root):
    path = os.getcwd()
    
    while root != os.path.basename(path):
        path = os.path.dirname(path)
        
    return path
    
#获取系统顶层目录路径，这里为：log_system
ROOT = get_root('pachong2')

#日志存放路径
LOG_PATH = os.path.join(ROOT, 'log')

#日志对象
LOG = None

#设置日志级别：NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
LOG_LEVEL = logging.DEBUG
