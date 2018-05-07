# -*- coding: utf-8 -*-

import requests
from config import config
from common.Generator import Generator
from TestData import EquipmentsBGetInfoData
from EquipmentsBGetBinding import EquipmentsBGetBinding


class EquipmentsBGetInfo(object):

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        self.EquipmentsBGetInfoData = EquipmentsBGetInfoData
        self.EquipmentsBGetBinding = EquipmentsBGetBinding()

    # 获取一体机的绑定、设备状态等信息
    def equipmentsb_getinfo(self):
        data = self.generator.set_default_params(self.EquipmentsBGetInfoData.GetInfo)
        data['EquipmentsE']['EquipmentsUID'] = self.config.EquipmentsUID
        response_data = self.generator.parse_response(self.EquipmentsBGetBinding.equipmentsb_getbinding())
        self.generator.update_secondlevelparameters(data, 'EquipmentsE', 'EnterpriseInfoGUID',
                                                    response_data['EnterpriseInfoE']['EnterpriseInfoGUID'])

        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(data),
                          headers=self.config.headers)
        print 'getinfo= ' + r.text
        return r.text


if __name__ == '__main__':
    h = EquipmentsBGetInfo()
    h.equipmentsb_getinfo()
