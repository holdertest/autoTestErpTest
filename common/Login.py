# -*- coding: utf-8 -*-

import requests
from config import config
import Generator
from TestData import TestData


class Login(object):
    _instance = None

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        self.set_cookie = ""
        self.headers = self.config.headers
        self.testdata = TestData

    def __new__(cls, *args, **kwargs):
        if Login._instance is None:
            Login._instance = object.__new__(cls, *args, **kwargs)
            super(Login, cls).__init__(cls)
        return Login._instance

    # 定义变量
    def login(self):
        r = requests.post(self.config.url_login,
                          self.generator.convert(self.testdata.AuthorizeCheck),
                          self.config.headers)
        try:
            self.generator.check_status(r.status_code)
        except:
            return False

        # self.set_cookie = r.headers['Set-Cookie']
        # self.headers.setdefault("Cookie", self.set_cookie)
        return self.headers
