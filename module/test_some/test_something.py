#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/21 11:14
# Author : LiuShiHua
# Desc :
import base64
import time

from module.test_some.type_util import *
import datetime

default_str = "AAhLqZL&amHoLhd";


def test_fun():
    res = '{"nowPage":2,"pageShow":2,"result":[{"evId":"214063838922809344","evOrder":"HTTP-003","isBind":0,"projectName":"花满楼（自用）","regCode":"31105101092011040043"},{"evId":"214063838952169472","evOrder":"HTTP-004","isBind":0,"projectName":"花满楼（自用）","regCode":"31105101092011040044"}],"start":2,"totalCount":15,"totalPage":8}'
    ev_base64_encode(res)


def ev_base64_encode(msg: str):
    token = base64.b64encode(msg.encode('UTF-8'))
    secret_msg = token.decode()
    print(secret_msg)
    day_num = datetime.datetime.now().day
    str_start = secret_msg[0:day_num]
    str_end = secret_msg[day_num:]
    result = str_start + default_str + str_end
    return result


def alarm_note_change():
    # 发送报警信息——给何先觉组
    from urllib.request import Request, urlopen
    url = 'http://api.t4.2012iot.com/api-chengdu-big-data/triggeralarmtips'
    req = Request(url=url, method='GET')
    result_content = urlopen(req).read().decode('utf-8')
    print(str(result_content))


format_ymdhms = "%Y-%m-%d %H:%M:%S"
format_ymdhm = "%Y-%m-%d %H:%M"
format_ymd = "%Y-%m-%d"

# 传入日期格式：[2018-12-11 11:12:12   2018-12-11 11:12  2018-12-11]
def getDateStrMillis(dateRes):
    try:
        if isinstance(dateRes, str):
            if dateRes.count(":") == 1:
                return time.mktime(time.strptime(dateRes, format_ymdhm))
            elif dateRes.count(":") == 2:
                return time.mktime(time.strptime(dateRes, format_ymdhms))
            else:
                return time.mktime(time.strptime(dateRes, format_ymd))
        else:
            return 0
    except:
        return 0

# 获取当前时间多少“秒钟”之前的时间datetime
def get_secounds_ago_datetime(secound:int):
    now = time.time() - secound
    return datetime.datetime.fromtimestamp(now)

# 获取今天00:00:00时间datetime
def get_today_00():
    return datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

if __name__ == '__main__':
    # test_fun()
    # alarm_note_change()
    now = getDateStrMillis(str(datetime.datetime.now()).split(".")[0])
    a7200= getDateStrMillis(str(get_secounds_ago_datetime(100)).split(".")[0])
    print(str(get_today_00()))
    print(type(now))
    print(str(now))
    print(type(a7200))
    print(str(a7200))
