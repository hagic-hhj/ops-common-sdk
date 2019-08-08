#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description：工具类

# @Time    : 2019/8/8 10:17
# @Author  : hubo
# @Email   : hagic.hhj@gmail.com
# @File    : tools.py


import sys
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor

#创建实现单例模式的装饰器
def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance

"""把输入转换为unicode，要求输入是unicode或者utf-8编码的bytes。"""
def bytes_to_unicode(input_bytes):
    if sys.version_info.major >= 3:
        #python3 实际上str(input_bytes, encoding='utf-8')=input_bytes.decode('utf-8')
        return str(input_bytes, encoding='utf-8')
    else:
        #python2
        return (input_bytes).decode('utf-8')

"""字典键值由str转为bytes"""
def convert(data):
    """若输入为bytes，则认为是utf-8编码，并返回utf8"""
    if isinstance(data, bytes):  return data.decode('utf8')
    """若输入为str（即unicode），则返回utf-8编码的bytes"""
    if isinstance(data, str):  return bytes(data, encoding='utf8')
    if isinstance(data, dict):   return dict(map(convert, data.items()))
    if isinstance(data, tuple):  return map(convert, data)
    if isinstance(data, list):  return [convert(i) for i in data]
    return data

"""检查密码复杂度"""
def check_password(data):
    return True if re.search("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$", data) and len(data) >= 8 else False

"""检查是否为邮箱地址"""
def is_mail(text, login_mail=None):
    if login_mail:
        if re.match(r'[0-9a-zA-Z_]{0,19}@%s' % login_mail, text):
            return True
        else:
            return False

    if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', text):
        return True
    else:
        return False

def is_tel(tel):
    ### 检查是否是手机号
    ret = re.match(r"^1[356789]\d{9}$", tel)
    if ret:
        return True
    else:
        return False

def check_contain_chinese(check_str):
    ### 检查是否包含汉字
    """
    :param check_str:
    :return:
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


class Executor(ThreadPoolExecutor):
    """ 线程执行类 """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, '_instance', None):
            cls._instance = ThreadPoolExecutor(max_workers=10)
        return cls._instance


def exec_shell(cmd):
    '''执行shell命令函数'''
    sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = sub.communicate()
    ret = sub.returncode
    if ret == 0:
        return ret, stdout.decode('utf-8').split('\n')
    else:
        return ret, stdout.decode('utf-8').replace('\n', '')
