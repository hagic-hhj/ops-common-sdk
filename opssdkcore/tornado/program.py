#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description：

# @Time    : 2019/8/16 16:43
# @Author  : hubo
# @Email   : hagic.hhj@gmail.com
# @File    : program.py

import fire


class MainProgram(object):
    def __init__(self, progressid=''):
        print(progressid)

    @staticmethod
    def run(cls_inst):
        if issubclass(cls_inst, MainProgram):
            fire.Fire(cls_inst)
        else:
            raise Exception('')