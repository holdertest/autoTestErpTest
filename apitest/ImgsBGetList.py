# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 0007 14:29
# @Author  : abel_sheng
# @File    : ImgsBGetList.py
# @Software: PyCharm

import requests
from config import config
from common.Generator import Generator
from TestData import ImgsBGetListData
from EquipmentsBGetBinding import EquipmentsBGetBinding
from StoreBGetList import StoreBGetList
from UserBNewLogin import UserBNewLogin


class ImgsBGetList(object):

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        self.EquipmentsBGetBinding = EquipmentsBGetBinding()
        self.StoreBGetList = StoreBGetList()
        self.UserBNewLogin = UserBNewLogin()
        self.ImgsBGetListData = ImgsBGetListData


    #
    def imgsb_getlist(self):
        data = self.generator.set_default_params(self.ImgsBGetListData.ImgsBGetList)
        get_binding_data = self.generator.parse_response(self.EquipmentsBGetBinding.equipmentsb_getbinding())
        self.generator.update_secondlevelparameters(data, 'ApiBase', 'MerID',
                                                    get_binding_data['EnterpriseInfoE']['EnterpriseInfoUID'])

        new_login_data = self.generator.parse_response(self.UserBNewLogin.userb_newlogin())
        self.generator.update_secondlevelparameters(data, 'ApiBase', 'UserGUID',
                                                    new_login_data['UsersE']['UsersGUID'])
        self.generator.update_secondlevelparameters(data, 'ImgsE', 'EnterpriseInfoGUID',
                                                    get_binding_data['EnterpriseInfoE']['EnterpriseInfoGUID'])

        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(data),
                          headers=self.config.headers)
        print 'imgsb_getlist= ' + r.text
        return r.text


if __name__ == "__main__":
    s = ImgsBGetList()
    s.imgsb_getlist()
