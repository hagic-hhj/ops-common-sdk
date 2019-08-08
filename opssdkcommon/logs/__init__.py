#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description：日志处理

# @Time    : 2019/8/6 14:41
# @Author  : hubo
# @Email   : hagic.hhj@gmail.com
# @File    : __init__1.py

import logging
import os

###写日志类
class Log:
    def __init__(self, log_flag='yunwei', log_file='/log/yunwei/yunwei.log'):
        self.logFlag = log_flag
        self.logFile = log_file

    def write_log(self, log_level, log_message):
        ###创建一个logger
        logger = logging.getLogger(self.logFlag)
        logger.setLevel(logging.DEBUG)

        ###建立日志目录
        log_dir = os.path.dirname(self.logFile)
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)

        ###创建一个handler用于写入日志文件
        fh = logging.FileHandler(self.logFile)
        fh.setLevel(logging.DEBUG)

        ###创建一个handler用于输出到终端
        th = logging.StreamHandler()
        th.setLevel(logging.DEBUG)

        ###定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s')
        fh.setFormatter(formatter)

        ###将相应的handler添加在logger对象中
        logger.addHandler(fh)
        logger.addHandler(th)

        ###开始记录日志
        level_dic = {'debug': logger.debug, 'info': logger.info, 'warning': logger.warning, 'error': logger.error,
                     'critical': logger.critical}

        ##最终如：logger.debug(log_message)
        level_dic[log_level](log_message)

        ###删除重复记录
        fh.flush()
        logger.removeHandler(fh)

        th.flush()
        logger.removeHandler(th)

if __name__ == "__main__":
    pass
