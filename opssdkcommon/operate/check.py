#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description：检查类

# @Time    : 2019/8/6 17:35
# @Author  : hubo
# @Email   : hagic.hhj@gmail.com
# @File    : check.py

import os
import socket
import fcntl
import struct
from opssdkcommon.operate import exec_shell

##目录空间剩余小于10返回false
def check_disk(d='/data', f=10):
    vfs = os.statvfs(d)
    available = vfs.f_bsize * vfs.f_bavail / 1024 / 1024 / 1024
    if available > f:
        return True
    return False


def check_sys_version():
    recode, res = exec_shell(
        "awk -F'release' '{print $2}' /etc/redhat-release | awk '{print $1}'|awk -F'.' '{print $1}'")
    return res[0]

#获取网卡 IPv4 地址
#https://www.cnblogs.com/my_life/articles/9187714.html
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', bytes(ifname[:15], 'utf-8'))
    )[20:24])
