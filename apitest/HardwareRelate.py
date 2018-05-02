# -*- coding: utf-8 -*-

import requests
import urllib
from config import config
from common.Generator import Generator
from TestData import TestData, HardwareRelateData


class HardwareRelate(object):
    _instance = None

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        # self.set_cookie = ""
        self.headers = self.config.headers
        self.testdata = TestData
        self.hardwarerelatedata = HardwareRelateData

    def __new__(cls, *args, **kwargs):
        if HardwareRelate._instance is None:
            HardwareRelate._instance = object.__new__(cls, *args, **kwargs)
            super(HardwareRelate, cls).__init__(cls)
        return HardwareRelate._instance

    # 定义变量
    def authorize_check(self):
        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(self.hardwarerelatedata.AuthorizeCheck),
                          headers=self.config.headers)
        # try:
        #     self.generator.check_status(r.status_code)
        #     print r.text
        # except:
        #     return False

        # self.set_cookie = r.headers['Set-Cookie']
        # self.headers.setdefault("Cookie", self.set_cookie)
        return r.text


if __name__ == '__main__':
    h = HardwareRelate()
    h.authorize_check()
