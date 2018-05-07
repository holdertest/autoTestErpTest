# -*- coding: utf-8 -*-

import requests
from config import config
from common.Generator import Generator
from TestData import UserBNewLoginData
from EquipmentsBGetBinding import EquipmentsBGetBinding
from StoreBGetList import StoreBGetList


class UserBNewLogin(object):

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        self.EquipmentsBGetBinding = EquipmentsBGetBinding()
        self.StoreBGetList = StoreBGetList()
        self.UserBNewLoginData = UserBNewLoginData

    # 登录
    def userb_newlogin(self):
        data = self.generator.set_default_params(self.UserBNewLoginData.NewLogin)
        get_binding_data = self.generator.parse_response(self.EquipmentsBGetBinding.equipmentsb_getbinding())
        self.generator.update_secondlevelparameters(data, 'UsersE', 'EnterpriseInfoGUID',
                                                    get_binding_data['EnterpriseInfoE']['EnterpriseInfoGUID'])
        self.generator.update_secondlevelparameters(data, 'ApiBase', 'MerID',
                                                    get_binding_data['EnterpriseInfoE']['EnterpriseInfoUID'])
        get_list_data = self.generator.parse_response(self.StoreBGetList.storeb_getlist())
        self.generator.update_secondlevelparameters(data, 'UsersE', 'StoreGUID',
                                                    get_list_data['ArrayOfStoreE'][self.config.Store_position_in_list][
                                                        'StoreGUID'])
        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(data),
                          headers=self.config.headers)
        print 'new_login= ' + r.text
        return r.text


if __name__ == "__main__":
    s = UserBNewLogin()
    s.userb_newlogin()