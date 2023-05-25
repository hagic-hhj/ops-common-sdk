#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description：setup module for core.

# @Time    : 2019/8/5 16:05
# @Author  : hubo
# @Email   : hagic.hhj@gmail.com
# @File    : setup.py


from setuptools import setup, find_packages
import os

PACKAGE = "opssdkcore"
NAME = "opssdkcore"
DESCRIPTION = "The core module of Python SDK."
AUTHOR = "hubo"
AUTHOR_EMAIL = "hagic.hhj@gmail.com"
URL = "https://github.com/hagic-hhj/opssdkcore"

TOPDIR = os.path.dirname(__file__) or "."
VERSION = __import__(PACKAGE).__version__

desc_file = open("README.rst")
try:
    LONG_DESCRIPTION = desc_file.read()
finally:
    desc_file.close()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache",
    url=URL,
    keywords=["ops", "sdk", "core"],
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires='>=3',
    platforms='any',
    install_requires=['fire', 'shortuuid', 'pymysql==0.9.3', 'sqlalchemy==1.3.0', 'python3-pika==0.9.14', 'PyJWT',
                      'Crypto==1.4.1', 'requests', 'redis==2.10.6', 'tornado==6.3.2',
                      'aliyun-python-sdk-core-v3==2.8.6', 'aliyun-python-sdk-dysmsapi', 'python-dateutil==2.7.5',
                      'ldap3==2.6', 'pycryptodome'],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
    )
)
