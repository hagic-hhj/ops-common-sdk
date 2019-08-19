#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description： 工具类

# @Time    : 2019/8/6 15:46
# @Author  : hubo
# @Email   : hagic.hhj@gmail.com
# @File    : __init__11.py


import time
from opssdkcore.logs import Log

log_path = '/log/yunwei/yunwei.log'
log_ins = Log('utils', log_path)

##计算函数运行时间
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        log_ins.write_log("info", '%s execute duration :%.3f second' % (str(func), duration))
        return result

    return wrapper