# -*- coding: utf-8 -*-

import pymssql, time
from GetConfig import GetConfig


class Sql(GetConfig):
    def __init__(self):
        super(Sql, self).__init__()
        pass

    def __connectDataBase(self, timeout=30):
        """
        #获取config文件中的数据，
        #连接到指定数据库，若连接失败，则等30s后重试，3次后放弃重连

        ==================================================
        create by : carl  date:2017-9-30

        last editor : carl  date:2017-9-30

        parameter : timeout

        return : cur

        usage : cur = __connectDataBase(timeout = 30)
        ==================================================
        """
        host, username, password, database = self.getDataBaseInfo()
        try:
            for i in range(1, 4):
                try:
                    self.conn = pymssql.connect(host=host,
                                                user=username,
                                                password=password,
                                                database=database,
                                                login_timeout=timeout)
                    break
                # timeout exception
                except Exception, e:
                    print "====Got error, try to reconnect, time %d====" % i
                    if i == 3:
                        err = "Connect to the host %s failed" % host
                        print err
                        return False

                    time.sleep(30)

            cur = self.conn.cursor()

            return cur
        except Exception, e:
            print e

    def execReadCommand(self, tablename):
        """
        #输入sql语句，获取语句执行的返回值

        ==================================================
        create by : carl  date:2017-9-30

        last editor : carl  date:2017-9-30

        parameter : tablename

        return : contens

        usage : contens = execReadCommand(tablename)
        ==================================================
        """

        try:
            #连接数据库
            cur = self.__connectDataBase()

            #执行sql
#             sql = "select * from %s"%tablename
            cur.execute(tablename)

            #读取contens
            contens = cur.fetchall()

            return contens
        except Exception, err:
            print "Error decoding config file: %s" % str(err)
        finally:
            cur.close()
            self.conn.close()

    def execInsertCommand(self, sql):
        """
        #输入sql语句，写入、修改表数据

        ==================================================
        create by : carl  date:2017-9-30

        last editor : carl  date:2017-9-30

        parameter : sql

        return : None

        usage : execInsertCommand(sql)
        ==================================================
        """

        try:
            #连接数据库
            cur = self.__connectDataBase()

            #执行sql
            cur.execute(sql)

            self.conn.commit()
        except Exception, err:
            print "Error decoding config file: %s" % str(err)
        finally:
            cur.close()
            self.conn.close()
