# -*- coding: utf-8 -*-

import requests
from config import config
from common.Generator import Generator
from TestData import EquipmentsBGetBindingData


class EquipmentsBGetBinding(object):

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        self.EquipmentsBGetBindingData = EquipmentsBGetBindingData

    # 获取一体机设备当前的绑定状态
    def get_binding(self):
        data = self.generator.set_default_params(self.EquipmentsBGetBindingData.GetBinding)
        data['EquipmentsE']['EquipmentsUID'] = self.config.EquipmentsUID
        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(data),
                          headers=self.config.headers)
        print 'get_binding= ' + r.text
        return r.text


if __name__ == '__main__':
    h = EquipmentsBGetBinding()
    h.get_binding()