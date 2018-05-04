# -*- coding: utf-8 -*-

import requests
from config import config
import common.Generator
from TestData import TestData


class Login(object):

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = common.Generator()
        self.set_cookie = ""
        self.headers = self.config.headers
        self.testdata = TestData

    # 登录接口
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
