# -*- coding: utf-8 -*-

import requests
from config import config
from common.Generator import Generator
from TestData import EquipmentsBAuthorizeCheckData


class EquipmentsBAuthorizeCheck(object):

    def __init__(self):
        # 创建测试套件
        self.config = config
        self.generator = Generator()
        self.EquipmentsBAuthorizeCheckData = EquipmentsBAuthorizeCheckData

    # 验证一体机授权使用权限，若验证失败，则不能使用一体机系统
    def authorize_check(self):
        data = self.generator.set_default_params(self.EquipmentsBAuthorizeCheckData.AuthorizeCheck)
        data['EquipmentsE']['EquipmentsUID'] = self.config.EquipmentsUID
        r = requests.post(url=self.config.url_base,
                          data=self.generator.convert(data),
                          headers=self.config.headers)
        print 'authorize_check= ' + r.text
        return r.text


if __name__ == '__main__':
    h = EquipmentsBAuthorizeCheck()
    h.authorize_check()
