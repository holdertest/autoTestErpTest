# coding=utf-8
'''
Created on 2017年9月18日

@author: Administrator
'''

import ConfigParser
import os


class GetConfig(object):
    """
    #该类用于存放获取配置文件相关操作的方法
    """

    def __init__(self):
        """
        #初始化configparser
        """
        super(GetConfig, self).__init__()
        self.config = ConfigParser.ConfigParser()

        self.path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.config_path = self.path + "\Config\Configuration.ini"

        self.config.read(self.config_path)

    def setOptionValue(self, section, option, value):
        """
        #设置config的值

        ==================================================
        create by : carl  date:2017-9-18

        last editor : carl  date:2017-9-18

        parameter : section -- section的名称
        parameter : option  -- section下option的名称
        parameter : value   -- 想要修改的值

        return : None

        usage : setOptionValue(section, option, value)
        ==================================================
        """
        self.config.set(section, option, value)
        self.config.write(open(self.config_path, 'w'))

    def getSingleSectionInfo(self, section, item):
        """
        #获取配置文件某section下某个option的值

        ==================================================
        create by : carl  date:2017-9-18

        last editor : carl  date:2017-9-18

        parameter : section -- section的名称
        parameter : item    -- section下item的名称

        return : info

        usage :info = getSingleSectionInfo("section", "item")
        ==================================================
        """

        # 判断参数section是否在配置文件中
        if section in self.config.sections():
            info = self.config.get(section, item)

        return info

    def getDataBaseInfo(self):
        """
        #获取配置文件中的数据库信息

        ==================================================
        create by : carl  date:2017-9-30

        last editor : carl  date:2017-9-30

        parameter : None

        return : host, username, password

        usage : host, username, password = getDataBaseInfo()
        ==================================================
        """
        host = self.getSingleSectionInfo("DataBase", "host")
        username = self.getSingleSectionInfo("DataBase", "username")
        password = self.getSingleSectionInfo("DataBase", "password")
        database = self.getSingleSectionInfo("DataBase", "database")

        return host, username, password, database

    def getLogPath(self):
        """
        #获取配置文件中的logpath

        ==================================================
        create by : carl  date:2017-9-30

        last editor : carl  date:2017-9-30

        parameter : None

        return : logpath

        usage : logpath = getLogPath()
        ==================================================
        """
        logpath = self.getSingleSectionInfo("LogPath", "logpath")

        return logpath

    def getUserInfo(self):
        """
        #获取配置文件中的userinfo

        ==================================================
        create by : carl  date:2017-9-30

        last editor : carl  date:2017-9-30

        parameter : None

        return : username, password

        usage : username, password = getUserInfo()
        ==================================================
        """
        username = self.getSingleSectionInfo("UserInfo", "username"),
        password = self.getSingleSectionInfo("UserInfo", "password")

        return username, password


if __name__ == "__main__":
    g = GetConfig()
    g.getSingleSectionInfo("1", "2")