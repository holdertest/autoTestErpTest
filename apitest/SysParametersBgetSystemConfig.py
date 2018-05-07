# -*- coding: utf-8 -*-

import requests
from config import config
from common.Generator import Generator
from TestData import StoreBGetListData, SysParametersBgetSystemConfigData
from EquipmentsBGetBinding import EquipmentsBGetBinding
from StoreBGetList import StoreBGetList
from UserBNewLogin import UserBNewLogin


class SysParametersBgetSystemConfig(object):

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        self.EquipmentsBGetBinding = EquipmentsBGetBinding()
        self.StoreBGetListData = StoreBGetListData
        self.StoreBGetList = StoreBGetList()
        self.UserBNewLogin = UserBNewLogin()
        self.SysParametersBgetSystemConfigData = SysParametersBgetSystemConfigData


    #
    def sysparametersb_getsystemconfig(self):
        data = self.generator.set_default_params(self.SysParametersBgetSystemConfigData.SysParametersBgetSystemConfig)
        get_binding_data = self.generator.parse_response(self.EquipmentsBGetBinding.equipmentsb_getbinding())
        self.generator.update_secondlevelparameters(data, 'ApiBase', 'MerID',
                                                    get_binding_data['EnterpriseInfoE']['EnterpriseInfoUID'])

        new_login_data = self.generator.parse_response(self.UserBNewLogin.userb_newlogin())
        self.generator.update_secondlevelparameters(data, 'ApiBase', 'UserGUID',
                                                    new_login_data['UsersE']['UsersGUID'])

        get_list_data = self.generator.parse_response(self.StoreBGetList.storeb_getlist())
        self.generator.update_secondlevelparameters(data, 'SysParametersE', 'StoreGUID',
                                                    get_list_data['ArrayOfStoreE'][self.config.Store_position_in_list][
                                                        'StoreGUID'])
        self.generator.update_secondlevelparameters(data, 'SysParametersE', 'EnterpriseInfoGUID',
                                                    get_binding_data['EnterpriseInfoE']['EnterpriseInfoGUID'])

        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(data),
                          headers=self.config.headers)
        print 'sysparametersb_getsystemconfig= ' + r.text
        return r.text


if __name__ == "__main__":
    s = SysParametersBgetSystemConfig()
    s.sysparametersb_getsystemconfig()
