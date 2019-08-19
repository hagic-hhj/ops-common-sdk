#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description：日志处理

# @Time    : 2019/8/6 14:41
# @Author  : hubo
# @Email   : hagic.hhj@gmail.com
# @File    : __init__1.py

import logging
from logging.handlers import TimedRotatingFileHandler
import os

#创建实现单例模式的装饰器 https://www.cnblogs.com/jiangxinyang/p/8454418.html
def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class FileLog:
    """
    1、以“a”（追加）的方式将日志输出到文件，如果文件不存在，则自动创建该文件
    2、该类无切割，可用supervisor 切割
    """
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

        ###定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s')
        fh.setFormatter(formatter)

        ###将相应的handler添加在logger对象中
        logger.addHandler(fh)

        ###开始记录日志
        level_dic = {'debug': logger.debug, 'info': logger.info, 'warning': logger.warning, 'error': logger.error,
                     'critical': logger.critical}

        ##最终如：logger.debug(log_message)
        level_dic[log_level](log_message)

        ###删除重复记录
        fh.flush()
        logger.removeHandler(fh)


@singleton
class ConsoleLog:
    """
    将日志输出到Stream，比如sys.stderr、sys.stdour、文件流等；即输出到控制台，可被supervisor捕获日志
    """
    def __init__(self, log_flag='yunwei'):
        self.logFlag = log_flag

    def write_log(self, log_level, log_message):
        ###创建一个logger
        logger = logging.getLogger(self.logFlag)
        logger.setLevel(logging.DEBUG)

        ###创建一个handler用于输出到终端
        th = logging.StreamHandler()
        th.setLevel(logging.DEBUG)

        ###定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s')
        th.setFormatter(formatter)

        ###将相应的handler添加在logger对象中
        logger.addHandler(th)

        ###开始记录日志
        level_dic = {'debug': logger.debug, 'info': logger.info, 'warning': logger.warning, 'error': logger.error,
                     'critical': logger.critical}

        ##最终如：logger.debug(log_message)
        level_dic[log_level](log_message)

        ###删除重复记录
        th.flush()
        logger.removeHandler(th)


@singleton
class TimedRotatingLog:
    """
    将日志输出到文件，可以通过设置时间，使日志根据不同的时间自动创建并输出到不同的文件中。
    """
    def __init__(self, log_flag='yunwei', logFile='/var/log/python/run.log'):
        self.logFlag = log_flag
        self.logFile = logFile

    def write_log(self, log_level, log_message):
        ###创建一个logger
        logger = logging.getLogger(self.logFlag)
        logger.setLevel(logging.DEBUG)

        ###建立日志目录
        log_dir = os.path.dirname(self.logFile)
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)

        ###创建一个handler用于写入日志文件
        handler = TimedRotatingFileHandler(self.logFile, when='D', interval=1, backupCount=7)
        handler.setLevel(logging.DEBUG)

        ###设置后缀名称，跟strftime的格式一样
        handler.suffix = "%Y%m%d.log"

        ###定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s')
        handler.setFormatter(formatter)

        ###将相应的handler添加在logger对象中
        logger.addHandler(handler)

        ###开始记录日志
        level_dic = {'debug': logger.debug, 'info': logger.info, 'warning': logger.warning, 'error': logger.error,
                     'critical': logger.critical}

        ##最终如：logger.debug(log_message)
        level_dic[log_level](log_message)

        ###删除重复记录
        handler.flush()
        logger.removeHandler(handler)


@singleton
class RotatingFileLog:
    """
    将日志输出到文件，可以通过设置文件大小，文件达到上限后自动创建一个新的文件来继续输出文件。
    """
    def __init__(self, log_flag='yunwei', logFile='/var/log/python/run.log'):
        self.logFlag = log_flag
        self.logFile = logFile

    def write_log(self, log_level, log_message):
        ###创建一个logger
        logger = logging.getLogger(self.logFlag)
        logger.setLevel(logging.DEBUG)

        ###建立日志目录
        log_dir = os.path.dirname(self.logFile)
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)

        ###创建一个handler用于写入日志文件
        handler = logging.handlers.RotatingFileHandler(self.logFile, mode="w", maxBytes=50000, backupCount=7, encoding="utf-8")
        handler.setLevel(logging.DEBUG)

        ###定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s')
        handler.setFormatter(formatter)

        ###将相应的handler添加在logger对象中
        logger.addHandler(handler)

        ###开始记录日志
        level_dic = {'debug': logger.debug, 'info': logger.info, 'warning': logger.warning, 'error': logger.error,
                     'critical': logger.critical}

        ##最终如：logger.debug(log_message)
        level_dic[log_level](log_message)

        ###删除重复记录
        handler.flush()
        logger.removeHandler(handler)

if __name__ == "__main__":
    pass
