#!/usr/bin/python
# -*- coding:gb2312 -*-

import os, sys
import logging

def get_root(root):
    path = os.getcwd()
    
    while root != os.path.basename(path):
        path = os.path.dirname(path)
        
    return path
    
#��ȡϵͳ����Ŀ¼·��������Ϊ��log_system
ROOT = get_root('pachong2')

#��־���·��
LOG_PATH = os.path.join(ROOT, 'log')

#��־����
LOG = None

#������־����NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
LOG_LEVEL = logging.DEBUG
