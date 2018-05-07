# -*- coding: utf-8 -*-

import requests
from config import config
from common.Generator import Generator
from TestData import StoreBGetListData
from EquipmentsBGetBinding import EquipmentsBGetBinding


class StoreBGetList(object):

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        self.EquipmentsBGetBinding = EquipmentsBGetBinding()
        self.StoreBGetListData = StoreBGetListData

    # 获取多个门店
    def storeb_getlist(self):
        data = self.generator.set_default_params(self.StoreBGetListData.GetList)
        get_binding_data = self.generator.parse_response(self.EquipmentsBGetBinding.equipmentsb_getbinding())
        self.generator.update_secondlevelparameters(data, 'StoreE', 'EnterpriseInfoGUID',
                                                    get_binding_data['EnterpriseInfoE']['EnterpriseInfoGUID'])
        self.generator.update_secondlevelparameters(data, 'ApiBase', 'MerID',
                                                    get_binding_data['EnterpriseInfoE']['EnterpriseInfoUID'])
        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(data),
                          headers=self.config.headers)
        print 'get_list= ' + r.text
        return r.text


if __name__ == "__main__":
    s = StoreBGetList()
    s.storeb_getlist()
