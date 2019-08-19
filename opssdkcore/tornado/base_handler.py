#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description：

# @Time    : 2019/8/16 17:43
# @Author  : hubo
# @Email   : hagic.hhj@gmail.com
# @File    : base_handler.py

import shortuuid
from tornado.web import RequestHandler, HTTPError


class BaseHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        #生成短的uuid,内部使用基于随机数的uuid4()来生成唯一的uudi,长度22
        self.new_csrf_key = str(shortuuid.uuid())
        self.user_id, self.username, self.nickname, self.email, self.is_super = None, None, None, None, False
        self.is_superuser = self.is_super

        super(BaseHandler, self).__init__(*args, **kwargs)

    def get_current_user(self):
        return self.username

    def get_current_id(self):
        return self.user_id

    def get_current_nickname(self):
        return self.nickname

    def get_current_email(self):
        return self.email

    def is_superuser(self):
        return self.is_superuser

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.set_status(status_code)
            return self.finish('找不到相关路径-404')

        elif status_code == 400:
            self.set_status(status_code)
            return self.finish('bad request.')

        elif status_code == 402:
            self.set_status(status_code)
            return self.finish('csrf error.')

        elif status_code == 403:
            self.set_status(status_code)
            return self.finish('Sorry, you have no permission. Please contact the administrator')

        elif status_code == 500:
            self.set_status(status_code)
            return self.finish('服务器内部错误')

        elif status_code == 401:
            self.set_status(status_code)
            return self.finish('你没有登录')

        else:
            self.set_status(status_code)


class LivenessProbe(RequestHandler):
    def head(self, *args, **kwargs):
        self.write("I'm OK")

    def get(self, *args, **kwargs):
        self.write("I'm OK")
