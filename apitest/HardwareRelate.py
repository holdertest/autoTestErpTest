# -*- coding: utf-8 -*-

import requests
from config import config
from common.Generator import Generator
from TestData import TestData, HardwareRelateData
import json


class HardwareRelate(object):
    _instance = None

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        # self.set_cookie = ""
        self.testdata = TestData
        self.hardwarerelatedata = HardwareRelateData

    def __new__(cls, *args, **kwargs):
        if HardwareRelate._instance is None:
            HardwareRelate._instance = object.__new__(cls, *args, **kwargs)
            super(HardwareRelate, cls).__init__(cls)
        return HardwareRelate._instance

    # 获取一体机设备当前的绑定状态
    def get_binding(self):
        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(self.hardwarerelatedata.GetBinding),
                          headers=self.config.headers)
        # try:
        #     self.generator.check_status(r.status_code)
        # except:
        #     return False

        # self.set_cookie = r.headers['Set-Cookie']
        # self.headers.setdefault("Cookie", self.set_cookie)

        s = json.loads(r.text)
        self.config.EnterpriseInfoID = s['EnterpriseInfoE']['EnterpriseInfoID']
        self.config.EnterpriseInfoUID = s['EnterpriseInfoE']['EnterpriseInfoUID']
        self.config.EnterpriseInfoGUID = s['EnterpriseInfoE']['EnterpriseInfoGUID']
        return r.text

    # 验证一体机授权使用权限，若验证失败，则不能使用一体机系统
    def authorize_check(self):
        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(self.hardwarerelatedata.AuthorizeCheck),
                          headers=self.config.headers)
        s = json.loads(r.text)
        self.config.EnterpriseInfoID = s['EnterpriseInfoE']['EnterpriseInfoID']
        self.config.EnterpriseInfoUID = s['EnterpriseInfoE']['EnterpriseInfoUID']
        self.config.EnterpriseInfoGUID = s['EnterpriseInfoE']['EnterpriseInfoGUID']
        return r.text

    # 获取一体机的绑定、设备状态等信息
    def get_info(self):
        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(
                              self.generator.update_enterpriseinfoe(self.hardwarerelatedata.GetInfo,
                                                                    'EnterpriseInfoGUID',
                                                                    self.config.EnterpriseInfoGUID)),
                          headers=self.config.headers)
        print r.text
        return r.text


if __name__ == '__main__':
    h = HardwareRelate()
    h.authorize_check()
    h.get_info()
