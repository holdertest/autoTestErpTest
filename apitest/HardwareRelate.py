# -*- coding: utf-8 -*-

import requests
import urllib
from config import config
from common.Generator import Generator
from TestData import TestData


class HardwareRelate(object):
    _instance = None

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        self.set_cookie = ""
        self.headers = self.config.headers
        self.testdata = TestData

    def __new__(cls, *args, **kwargs):
        if HardwareRelate._instance is None:
            HardwareRelate._instance = object.__new__(cls, *args, **kwargs)
            super(HardwareRelate, cls).__init__(cls)
        return HardwareRelate._instance

    # 定义变量
    def AuthorizeCheck(self):
        r = requests.post(self.config.url_login, urllib.quote(self.generator.convert(self.testdata.AuthorizeCheck)),
                          headers=self.config.headers)
        try:
            self.generator.check_status(r.status_code)
        except:
            return False

        # self.set_cookie = r.headers['Set-Cookie']
        # self.headers.setdefault("Cookie", self.set_cookie)
        return self.headers

