# coding=utf-8

'''
Created on 2017年9月29日

@author: holder
'''
import string
import json
import hashlib
import random
from config import config


class Generator(object):
    """
    ---------------------------------------------------------------
    #参数规则，example：
    1.FirstLetterUppercase      ---- 表示参数需要首字母大写
    2.NumberOnly                ---- 表示参数只含有数字，且是两位数
    3.CharOnly                  ---- 表示参数只含有字母，且是8位长度
    4.NoSpecial                 ---- 表示参数没有特殊字符
    5.CharSpecialInclude        ---- 表示参数字母和特殊字符组成
    6.NumberSpecialInclude      ---- 表示参数由数字和特殊字符组成
    7.All                       ---- 表示参数无限制
    
    *Note：
    1.规则1可以分别与3、4、7配合使用
    2.规则2、4、5、6只能单独使用
    3.规则3可与1配合使用
    4.规则4可与6配合使用
    5.规则5可与6配合使用
    6.默认选择6
    7.2、3不接数字，默认16位
    ---------------------------------------------------------------
    """

    def __init__(self):
        '''
        Constructor
        '''
        super(Generator, self).__init__()
        self.SPECIAL_LIST = [i for i in string.punctuation]
        self.CHAR_LIST = [i for i in string.letters]
        self.NUMBER_LIST = [i for i in string.digits]
        self.config = config

        self.LIST_MODEL = [self.SPECIAL_LIST, self.CHAR_LIST, self.NUMBER_LIST]

    def traversalAllKeyRules(self, kw):
        """
        #该函数用于生成接口功能的参数
        #参数为接口参数的框架
        #返回值为生成的接口参数
        
        ==================================================
        create by : carl  date:2017-9-27
        
        last editor : carl  date:2017-10-9
        
        parameter : kw
        
        return : kw
        
        usage : kw = traversalAllKeyRules(kw)
        ==================================================
        """
        if isinstance(kw, dict):
            for key, value in kw.items():
                if isinstance(value, dict) or isinstance(value, list):
                    self.traversalAllKeyRules(value)
                else:
                    if isinstance(value, str):
                        str_value = self.generateTestData(value)
                        if str_value != "":
                            kw[key] = str_value

        elif isinstance(kw, list):
            for item in kw:
                if isinstance(item, dict) or isinstance(item, list):
                    self.traversalAllKeyRules(item)

        return kw

    def generateTestData(self, str_rule, number=None):
        """
        #根绝str_rule规则，创建字符串信息
        
        ==================================================
        create by : carl  date:2017-9-27
        
        last editor : carl  date:2017-10-9
        
        parameter : number
        
        return : str_value
        
        usage : str_value = generateTestData(str_rule, number = None)
        ==================================================
        """

        str_value = ""

        if number == None:
            number = random.randrange(8, 17)
        else:
            number = int(number)
            if number < 8: number = 8

        if len(str_rule.split(",")) >= 2:
            str_rule = str_rule.split(",")[random.randrange(0, len(str_rule.split(",")))].strip()

        if "FirstLetterUppercase" in str_rule:
            if "CharOnly" in str_rule:
                str_value = self.generateCharOnlyAndFirstLetterUpper(number)
            elif "NoSpecial" in str_rule:
                str_value = self.generateFirstLetterUpperAndNoSpecial(number)
            elif "Number" in str_rule:
                str_value = self.generateFirstLetterUpperAndNumbers(number)
            else:
                str_value = self.generateFirstLetterUpper(number)

            return str_value
        elif "NumberOnly" in str_rule:
            str_value = self.generateNumberOnly(number)
        elif "CharOnly" in str_rule:
            str_value = self.generateCharOnly(number)
        elif "NoSpecial" in str_rule:
            str_value = self.generateNoSpecial(number)
        elif "CharSpecialInclude" in str_rule:
            str_value = self.generateCharAndSpecial(number)
        elif "NumberSpecialInclude" in str_rule:
            str_value = self.generateNumberAndSpecial(number)
        elif "All" in str_rule:
            str_value = self.generateAllRule(number)

        return str_value

    def generateFirstLetterUpperAndNumbers(self, number):
        """
        #创建首字母大写+数字的字符串
        
        ==================================================
        create by : carl  date:2017-9-27
        
        last editor : carl  date:2017-10-9
        
        parameter : number
        
        return : str_value
        
        usage : str_value = generateCharOnlyAndFirstLetterUpper(number)
        ==================================================
        """

        str_value = ""
        number = int(number)

        for item in range(0, number):
            if item == 0:
                str_value += self.CHAR_LIST[random.randrange(27, 52)]
            else:
                str_value += self.CHAR_LIST[random.randrange(0, len(self.NUMBER_LIST))]

        return str_value

    def generateNoSpecial(self, number):
        """
        #创建没有特殊字符的字符串
        
        ==================================================
        create by : carl  date:2017-9-27
        
        last editor : carl  date:2017-10-9
        
        parameter : number
        
        return : str_value
        
        usage : str_value = generateNoSpecial(number)
        ==================================================
        """

        str_value = ""
        number = int(number)
        loop = 0
        while loop < number:
            value = random.randrange(1, len(self.LIST_MODEL))
            str_value += self.LIST_MODEL[value][random.randrange(0, len(self.LIST_MODEL[value]))]
            loop += 1

        return str_value

    def generateCharOnlyAndFirstLetterUpper(self, number):
        """
        #创建首字母大写的全字母字符串
        
        ==================================================
        create by : carl  date:2017-9-27
        
        last editor : carl  date:2017-10-9
        
        parameter : number
        
        return : str_value
        
        usage : str_value = generateCharOnlyAndFirstLetterUpper(number)
        ==================================================
        """

        str_value = ""
        number = int(number)

        for item in range(0, number):
            if item == 0:
                str_value += self.CHAR_LIST[random.randrange(27, 52)]
            else:
                str_value += self.CHAR_LIST[random.randrange(0, len(self.CHAR_LIST))]

        return str_value

    def generateFirstLetterUpperAndNoSpecial(self, number):
        """
        #创建首字母大写，没有特殊字符的字符串
        
        ==================================================
        create by : carl  date:2017-9-27
        
        last editor : carl  date:2017-10-9
        
        parameter : number
        
        return : str_value
        
        usage : str_value = generateFirstLetterUpperAndNoSpecial(number)
        ==================================================
        """

        str_value = ""
        number = int(number)

        for item in range(0, number):
            if item == 0:
                str_value += self.CHAR_LIST[random.randrange(27, 52)]
            else:
                value = random.randrange(1, len(self.LIST_MODEL))
                str_value += self.LIST_MODEL[value][random.randrange(0, len(self.LIST_MODEL[value]))]

        return str_value

    def generateFirstLetterUpper(self, number):
        """
        #生成首字母大写的字符串
        
        ==================================================
        create by : carl  date:2017-9-27
        
        last editor : carl  date:2017-10-9
        
        parameter : number
        
        return : str_value
        
        usage : str_value = generateFirstLetterUpper(number)
        ==================================================
        """

        str_value = ""
        number = int(number)

        for item in range(0, number):
            if item == 0:
                str_value += self.CHAR_LIST[random.randrange(27, 52)]
            else:
                value = random.randrange(0, len(self.LIST_MODEL))
                str_value += self.LIST_MODEL[value][random.randrange(0, len(self.LIST_MODEL[value]))]

        return str_value

    def generateNumberOnly(self, number):
        """
        #生成全数字的字符串
        
        ==================================================
        create by : carl  date:2017-9-27
        
        last editor : carl  date:2017-10-9
        
        parameter : number
        
        return : str_value
        
        usage : str_value = generateNumberOnly(number)
        ==================================================
        """

        str_value = ""
        number = int(number)
        loop = 0

        while loop < number:
            str_value += self.NUMBER_LIST[random.randrange(0, len(self.NUMBER_LIST))]
            loop += 1

        return str_value

    def generateCharOnly(self, number):
        """
        #生成全字母的字符串
        
        ==================================================
        create by : carl  date:2017-9-27
        
        last editor : carl  date:2017-10-9
        
        parameter : number
        
        return : str_value
        
        usage : str_value = generateCharOnly(number)
        ==================================================
        """

        str_value = ""
        number = int(number)
        loop = 0

        while loop < number:
            str_value += self.CHAR_LIST[random.randrange(0, len(self.CHAR_LIST))]
            loop += 1

        return str_value

    def generateCharAndSpecial(self, number):
        """
        #生成字母+特殊字符的字符串
        
        ==================================================
        create by : carl  date:2017-9-27
        
        last editor : carl  date:2017-10-9
        
        parameter : number
        
        return : str_value
        
        usage : str_value = generateCharAndSpecial(number)
        ==================================================
        """

        str_value = ""
        number = int(number)

        for item in range(0, number):
            item = random.randrange(0, 2)
            str_value += self.LIST_MODEL[item][random.randrange(0, len(self.LIST_MODEL[item]))]

        return str_value

    def generateNumberAndSpecial(self, number):
        """
        #生成数字+特殊字符的字符串
        
        ==================================================
        create by : carl  date:2017-9-27
        
        last editor : carl  date:2017-10-9
        
        parameter : number
        
        return : str_value
        
        usage : str_value = generateNumberAndSpecial(number)
        ==================================================
        """

        str_value = ""
        number = int(number)
        list_value = [0, 2]

        for item in range(0, number):
            item = random.randrange(0, 2)
            str_value += self.LIST_MODEL[list_value[item]][random.randrange(0, len(self.LIST_MODEL[list_value[item]]))]

        return str_value

    def generateAllRule(self, number):
        """
        #生成任意字符串
        
        ==================================================
        create by : carl  date:2017-9-27
        
        last editor : carl  date:2017-10-9
        
        parameter : number
        
        return : str_value
        
        usage : str_value = generateAllRule(number)
        ==================================================
        """

        str_value = ""
        number = int(number)

        for item in range(0, number):
            item = random.randrange(0, 3)
            str_value += self.LIST_MODEL[item][random.randrange(0, len(self.LIST_MODEL[item]))]

        return str_value

    def convert(self, data):
        data = self.update_dict(data, self.get_nonceStr(16, 32))
        json_dump = json.dumps(data)
        json_signed = self.sign(json_dump, self.config.UNSIGN_KEY) + "$" + json_dump
        return json_signed

    def sign(self, str_data, key):
        data = str_data.lower()
        data = data + "&key=" + key
        return self.get_md5hash(data)

    @staticmethod
    def get_md5hash(str_data):
        m1 = hashlib.md5()
        m1.update(str_data.encode('utf-8'))
        return m1.hexdigest()

    '''
        获取NonceStr
    '''
    @staticmethod
    def get_nonceStr(num_min, num_max):
        s1 = tuple(
            ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v",
             "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
             "R",
             "S",
             "T", "U", "V", "W", "X", "Y", "Z"))
        str1 = ""
        num = random.randint(0, num_max) % (num_max - num_min + 1) + num_min
        for index in range(num):
            num1 = random.randint(0, len(s1)) % (len(s1) - 1)
            str1 = str1 + s1[num1]
        return str1

    '''
        更新参数中的NonceStr
    '''
    @staticmethod
    def update_dict(dict1={}, value=''):
        dict1["NonceStr"] = value
        return dict1

    @staticmethod
    def check_status(status):
        if status != 200:
            raise AssertionError('%s != 200' % status)
        else:
            print "login success"

# if __name__ == "__main__":
#     s = Generator()
#     dict1 = {
#         "ErrorCode": 0,
#         "Data": {
#             "Code": "CharOnly",
#             "Data": [
#                 {
#                     "MemberGUID": "3a6acca8-95b9-49d8-87ed-061571218ffc",
#                     "MemberName": "aaa",
#                     "MemberGroup": 0,
#                     "MemberStatus": 0,
#                     "yes": "CharOnly,NumberOnly",
#                 }
#             ]
#         }
#     }
#     kw = s.traversalAllKeyRules(dict1)
#     print s.generateAllRule(8)
