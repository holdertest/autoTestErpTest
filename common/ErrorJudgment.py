# -*- coding: utf-8 -*-
import sys
reload(sys)  # 2
sys.setdefaultencoding('utf-8')


class ErrorJudgment(object):
    _instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if ErrorJudgment._instance is None:
            ErrorJudgment._instance = object.__new__(cls, *args, **kwargs)
            super(ErrorJudgment, cls).__init__(cls)
        return ErrorJudgment._instance

    @staticmethod
    def common_check_code(r):
        response = r.json()
        if response["ErrorCode"] != 0:
            raise AssertionError('Add failure, status_code: %s, ErrorCode: %s' % (r.status_code, response["ErrorCode"]))
        elif response["Data"]["Code"] != 0:
            raise AssertionError('Add failure, %s' % response["Data"]["Data"])
        else:
            print response["Data"]
        pass





