'''headers = {
            'Content-type': 'application/x-www-form-urlencoded',
        }
data = {'username': '11111111111', 'userPwd': 'e3ceb5881a0a1fdaad01296d7554868d', 'vcode': ''}

url_login = "http://www.heserp.com/Handler/Login.ashx"
url_warehouseAdd = "http://bs01.heserp.com/modules/CKLX/?WarehouseTypeAdd"
url_warehouseQuery = "http://bs01.heserp.com/modules/CKLX/?WarehouseTypeQuery"'''
from common import tool;

headers = {'Content-Length':'425',
           'Host':'115.29.175.3:82',
           'Connection':'Keep-Alive',
           'Accept-Encoding':'gzip',
            'User-Agent':'okhttp/3.9.0'
        }
str=tool.get_str(16,32)
data='''{"ApiBase":{"BackType":"1","Method":"EquipmentsB.AuthorizeCheck","Model":"FrontendB_Public","TerminalID":"04347f2465200cfe","TerminalType":20,"Version":0},"AppVersion":{"VersionType":1},"EquipmentsE":{"EnterpriseInfoGUID":"2fc6e701-cdc2-41b8-8a3f-ffc66c3489fb","EquipmentsUID":"04347f2465200cfe","StoreGUID":"5f55e93c-9fa7-41c2-8ed7-ec615681f7fe"},"NonceStr":"'''+str+'''","PageInfo":{}}
'''
login_data = '''{
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
    # "NonceStr": "",
    "PageInfo": {}
 }'''
login_data2=tool.convert(data)

print(login_data2)
# url_login = "http://www.heserp.com/Handler/Login.ashx"
url_login = "http://115.29.175.3:82/AIO/Frontend.ashx/ "
url_warehouseAdd = "http://bs01.heserp.com/modules/CKLX/?WarehouseTypeAdd"
url_warehouseQuery = "http://bs01.heserp.com/modules/CKLX/?WarehouseTypeQuery"


