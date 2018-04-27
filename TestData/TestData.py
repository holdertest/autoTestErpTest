# -*- coding: utf-8 -*-
####################################################
#    公共数据
#    term 查询条件
####################################################
term = {"Conditions": [], "Pager": {"CurrentPage": 1}}

#####################################################
#    仓库类型数据
#    addWarehouseType 新增仓库类型数据
#####################################################
addWarehouseType = [
    {
        "WarehouseTypeName": "TestCase_5",
        "Remark": "Remark_1"
    },
    {
        "WarehouseTypeName": "TestCase_6",
        "Remark": "Remark_2"
    }
]

AuthorizeCheck = {
    "ApiBase": {
        "BackType": "1",
        "Method": "EquipmentsB.AuthorizeCheck",
        "Model": "FrontendB_Public",
        "TerminalID": "04347f2465200cfe",
        "TerminalType": 20,
        "Version": 0
    },
    "AppVersion": {
        "VersionType": 1
    },
    "EquipmentsE": {
        "EnterpriseInfoGUID": "2fc6e701-cdc2-41b8-8a3f-ffc66c3489fb",
        "EquipmentsUID": "04347f2465200cfe",
        "StoreGUID": "5f55e93c-9fa7-41c2-8ed7-ec615681f7fe"
    },
    "NonceStr": "'''+str+'''",
    "PageInfo": {}
}