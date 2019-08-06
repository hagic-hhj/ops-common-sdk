#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description：

# @Time    : 2019/8/5 16:05
# @Author  : hubo
# @Email   : hagic.hhj@gmail.com
# @File    : setup.py

from distutils.core import setup

setup(
    name='opssdkcommon',
    version='0.0.1',
    packages=['opssdkcommon', 'opssdkcommon.logs', 'opssdkcommon.operate', 'opssdkcommon.install', 'opssdkcommon.get_info', 'opssdkcommon.utils', 'websdk'],
    url='https://github.com/hagic-hhj/opssdkcommon/',
    license='',
    install_requires=['fire', 'shortuuid', 'pymysql==0.9.3', 'sqlalchemy==1.3.0', 'python3-pika==0.9.14', 'PyJWT',
                      'Crypto==1.4.1', 'requests', 'redis==2.10.6', 'tornado==5.0',
                      'aliyun-python-sdk-core-v3==2.8.6', 'aliyun-python-sdk-dysmsapi', 'python-dateutil==2.7.5',
                      'ldap3==2.6', 'pycryptodome'],
    author='hubo',
    author_email='hagic.hhj@gmail.com',
    description='SDK of the operation and maintenance script'
                'logs'
                'operate'
)
