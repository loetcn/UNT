#!/usr/bin/python
# -*- coding:gb2312 -*-

import os
import time
import logging

from meituan.public import config

def init_log(logger_name, log_name):
    #cut_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    #file_name = os.path.join(config.LOG_PATH, log_name + cut_time + '.log')
    try:

        file_name = os.path.join(config.LOG_PATH, log_name + '.log')
        logger = logging.getLogger(logger_name)
        logger.setLevel(config.LOG_LEVEL)

        fh = logging.FileHandler(file_name)
        fh.setLevel(config.LOG_LEVEL)

        formatter = logging.Formatter('[%(module)s] %(asctime)s - [%(message)s]')
        fh.setFormatter(formatter)

        logger.addHandler(fh)

        config.LOG = logger

    except:

        logger = logging.getLogger(logger_name)
        logger.setLevel(config.LOG_LEVEL)

        fh = logging.FileHandler(config.LOG_PATH, log_name + '.log')
        fh.setLevel(config.LOG_LEVEL)
        formatter = logging.Formatter('[%(module)s] %(asctime)s - [%(message)s]')
        fh.setFormatter(formatter)

        logger.addHandler(fh)

        config.LOG = logger
    return 

def logger(namer ,file ):

    if namer == '__main__':
        name = os.path.basename(file)
        init_log(name, name)
