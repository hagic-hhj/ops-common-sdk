#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description：定制 Application

# @Time    : 2019/8/7 10:18
# @Author  : hubo
# @Email   : hagic.hhj@gmail.com
# @File    : application.py

from shortuuid import uuid
from tornado import httpserver, ioloop
from tornado import options as tnd_options
from tornado.options import options, define
from tornado.web import Application as tornadoApp
from .web_logs import ins_log

from .configs import configs

#用来定义options选项变量的方法，定义的变量可以在全局的tornado.options.options中获取使用
#当前tornado.options.options.port = options.port
define("addr", default='0.0.0.0', help="run on the given ip address", type=str)
define("port", default=8000, help="run on the given port", type=int)
define("progid", default=str(uuid()), help="tornado progress id", type=str)


class Application(tornadoApp):
    """ 定制 Tornado Application 集成日志、sqlalchemy 等功能 """


    def __init__(self, handlers=None, default_host="", transforms=None, **settings):
        """等价于
        #自定义应用
        class MyApplication(tornado.web.Application):
        def __init__(self, urls, configs):
        super(MyApplication, self).__init__(handlers=urls, **configs)
        #创建服务器
        tornado.options.parse_command_line()
        http_server = tornado.httpserver.HTTPServer(MyApplication(urls,configs))
        http_server.listen(options.port)
        import tornado.ioloop
        tornado.ioloop.IOLoop.current().start()
        #https://www.e-learn.cn/content/qita/949678
        """

        #转换命令行参数，并将转换后的值对应的设置到全局options对象相关属性上。追加命令行参数的方式是--myoption=myvalue
        tnd_options.parse_command_line()
        if configs.can_import:
            configs.import_dict(**settings)
        ins_log.read_log('info', '%s' % options.progid)
        super(Application, self).__init__(handlers, default_host, transforms, **configs)
        http_server = httpserver.HTTPServer(self)
        http_server.listen(options.port, address=options.addr)
        self.io_loop = ioloop.IOLoop.instance()

    def start_server(self):
        """
        启动 tornado 服务
        :return:
        不想在异常发生时结束程序，只需在try里捕获它。
        """
        try:
            ins_log.read_log('info', 'progressid: %(progid)s' % dict(progid=options.progid))
            ins_log.read_log('info', 'server address: %(addr)s:%(port)d' % dict(addr=options.addr, port=options.port))
            ins_log.read_log('info', 'web server start sucessfuled.')
            self.io_loop.start()
        except KeyboardInterrupt:
            self.io_loop.stop()
        except:
            import traceback
            #1、print_exc()：是对异常栈输出
            #2、format_exc()：是把异常栈以字符串的形式返回，print(traceback.format_exc()) 就相当于traceback.print_exc()
            #3、print_exception()：traceback.print_exc()实现方式就是traceback.print_exception(sys.exc_info())，可以点sys.exc_info()进去看看实现
            ins_log.read_log('error', '%(tra)s' % dict(tra=traceback.format_exc()))


if __name__ == '__main__':
    pass
