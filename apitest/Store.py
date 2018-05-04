# -*- coding: utf-8 -*-

import requests
from config import config
from common.Generator import Generator
from TestData import StoreData
from HardwareRelate import HardwareRelate


class Store(object):

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        self.hardwarerelate = HardwareRelate()
        self.storedata = StoreData

    # 获取多个门店
    def get_list(self):
        data = self.generator.set_default_params(self.storedata.GetList)
        response_data = self.generator.parse_response(self.hardwarerelate.get_binding())
        self.generator.update_secondlevelparameters(data, 'StoreE', 'EnterpriseInfoGUID',
                                                    response_data['EnterpriseInfoE']['EnterpriseInfoGUID'])
        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(data),
                          headers=self.config.headers)
        print 'get_list= ' + r.text
        return r.text


if __name__ == "__main__":
    s = Store()
    s.get_list()
