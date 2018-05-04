# -*- coding: utf-8 -*-

import requests
from config import config
from common.Generator import Generator
from TestData import HardwareRelateData


class HardwareRelate(object):

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        self.hardwarerelatedata = HardwareRelateData

    # 获取一体机设备当前的绑定状态
    def get_binding(self):
        data = self.generator.set_default_params(self.hardwarerelatedata.GetBinding)
        data['EquipmentsE']['EquipmentsUID'] = self.config.EquipmentsUID
        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(data),
                          headers=self.config.headers)
        print 'get_binding= ' + r.text
        return r.text

    # 验证一体机授权使用权限，若验证失败，则不能使用一体机系统
    def authorize_check(self):
        data = self.generator.set_default_params(self.hardwarerelatedata.AuthorizeCheck)
        data['EquipmentsE']['EquipmentsUID'] = self.config.EquipmentsUID
        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(data),
                          headers=self.config.headers)
        print 'authorize_check= ' + r.text
        return r.text

    # 获取一体机的绑定、设备状态等信息
    def get_info(self):
        data = self.generator.set_default_params(self.hardwarerelatedata.GetInfo)
        data['EquipmentsE']['EquipmentsUID'] = self.config.EquipmentsUID
        response_data = self.generator.parse_response(self.get_binding())
        self.generator.update_secondlevelparameters(data, 'EquipmentsE', 'EnterpriseInfoGUID',
                                                    response_data['EnterpriseInfoE']['EnterpriseInfoGUID'])

        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(data),
                          headers=self.config.headers)
        print 'getinfo= ' + r.text
        return r.text


if __name__ == '__main__':
    h = HardwareRelate()
    h.get_binding()
    h.authorize_check()
    h.get_info()
