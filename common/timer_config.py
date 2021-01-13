#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/8 17:17
# Author : LiuShiHua
# Desc :
import datetime

def send_maintenance_msg():
    print(str(datetime.datetime.now()) + ":发送维保信息")


def send_maintenance_msg1():
    print(str(datetime.datetime.now()) + ":发送维保信息——————")


class TimerConfig(object):
    # 其中id是一个标识，func指定定时执行的函数，args指定输入参数列表，trigger指定任务类型，
    # 如interval表示时间间隔，具体参见APScheduler相关说明。seconds表示时间周期，单位是秒。
    JOBS = [
        {
            'id': 'wx_wo_notice',
            'func': send_maintenance_msg,
            'args': None,
            'trigger': 'interval',
            'seconds': 10
        }
    ]
