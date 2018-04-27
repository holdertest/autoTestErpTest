# -*- coding: utf-8 -*-
import requests
import json
from common.ErrorJudgment import ErrorJudgment
# from common.Login import Login
import config.config as CONFIG
import TestData.TestData as TestData


class Warehouse(object):
    def __init__(self):
        super(Warehouse, self).__init__()
        self.config = CONFIG
        self.check_func = ErrorJudgment()

    def add_warehouse_type(self, headers, warehouse_type_name=[]):
        add_warehouse_type_list = []
        if not warehouse_type_name:
            add_warehouse_type_list = TestData.addWarehouseType
        else:
            for string in warehouse_type_name:
                add_warehouse_type_list.append(
                    {
                        "WarehouseTypeName": string,
                        "Remark": "Remark_1"
                    }
                )
        for form in add_warehouse_type_list:
            r = requests.post(self.config.url_warehouseAdd,
                              data={"WarehouseType": json.dumps(form)},
                              headers=headers)
            self.check_func.common_check_code(r)

    def query_warehouse_type(self, headers):
        term = TestData.term
        r = requests.post(self.config.url_warehouseQuery,
                          data={"term": json.dumps(term)},
                          headers=headers)
        self.check_func.common_check_code(r)

    def aaa(self, value):
        print value

if __name__ == '__main__':
    pass
    # a = Login()
    # b = a.login()
    # w = Warehouse()
    # w.add_warehouse_type(b)