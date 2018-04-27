# -*- coding: utf-8 -*-

import requests
import urllib
import config.config as CONFIG


class Login(object):
    _instance = None

    def __init__(self):
        # 创建测试套件
        self.config = CONFIG
        self.set_cookie = ""
        self.headers = self.config.headers

    def __new__(cls, *args, **kwargs):
        if Login._instance is None:
            Login._instance = object.__new__(cls, *args, **kwargs)
            super(Login, cls).__init__(cls)
        return Login._instance

    # 定义变量
    def login(self):
        r = requests.post(self.config.url_login, urllib.quote(self.config.login_data2), headers=self.config.headers)
        try:
            self.check_status(r.status_code)
        except:
            return False

        # self.set_cookie = r.headers['Set-Cookie']
        # self.headers.setdefault("Cookie", self.set_cookie)
        return self.headers

    def check_status(self, status):
        if status != 200:
            raise AssertionError('%s != 200' % status)
        else:
            print "login success"
