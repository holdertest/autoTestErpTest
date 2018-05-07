# -*- coding: utf-8 -*-

import requests
from config import config
from common.Generator import Generator
from TestData import StoreBGetListData, UsersBGetListData
from EquipmentsBGetBinding import EquipmentsBGetBinding
from StoreBGetList import StoreBGetList
from UserBNewLogin import UserBNewLogin


class UsersBGetList(object):

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        self.EquipmentsBGetBinding = EquipmentsBGetBinding()
        self.StoreBGetListData = StoreBGetListData
        self.StoreBGetList = StoreBGetList()
        self.UserBNewLogin = UserBNewLogin()
        self.UsersBGetListData = UsersBGetListData


    #
    def usersb_getlist(self):
        data = self.generator.set_default_params(self.UsersBGetListData.UsersBGetList)
        get_binding_data = self.generator.parse_response(self.EquipmentsBGetBinding.equipmentsb_getbinding())
        self.generator.update_secondlevelparameters(data, 'ApiBase', 'MerID',
                                                    get_binding_data['EnterpriseInfoE']['EnterpriseInfoUID'])

        new_login_data = self.generator.parse_response(self.UserBNewLogin.userb_newlogin())
        self.generator.update_secondlevelparameters(data, 'ApiBase', 'UserGUID',
                                                    new_login_data['UsersE']['UsersGUID'])
        self.generator.update_secondlevelparameters(data, 'UsersE', 'EnterpriseInfoGUID',
                                                    get_binding_data['EnterpriseInfoE']['EnterpriseInfoGUID'])

        get_list_data = self.generator.parse_response(self.StoreBGetList.storeb_getlist())
        self.generator.update_secondlevelparameters(data, 'UsersE', 'StoreGUID',
                                                    get_list_data['ArrayOfStoreE'][self.config.Store_position_in_list][
                                                        'StoreGUID'])
        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(data),
                          headers=self.config.headers)
        print 'usersb_getlist= ' + r.text
        return r.text


if __name__ == "__main__":
    s = UsersBGetList()
    s.usersb_getlist()