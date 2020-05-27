#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/8/17 10:52
# Author : LiuShiHua
# Desc :
import time
import calendar
from datetime import timedelta, datetime, date

format_ymdhms = "%Y-%m-%d %H:%M:%S"
format_ymdhm = "%Y-%m-%d %H:%M"
format_ymd = "%Y-%m-%d"

format_ymdhms_ = "%Y%m%d%H%M%S"


# datetime.strptime(str(date数据), format_ymd)  —— date 转 datetime
# [datetime数据].strftime(format_ymdhms) —— datetime 时间格式化

# 数据库时间 转 str
def db_datetime_to_str(dbtime):
    if isinstance(dbtime, datetime) or isinstance(dbtime, date):
        return str(dbtime)
    return dbtime


# 获取当前时间的一年后的时间
# 若是 闰年2月29号 一年后 取2月28号
def get_thistime_nextyear(resdatetime: datetime):
    if resdatetime.month == 2 and resdatetime.day == 29:
        return resdatetime.replace(year=(resdatetime.year + 1), day=28)
    return resdatetime.replace(year=(resdatetime.year + 1))


# 获取当前时间的 daynum 天“后”的时间
def days_after_time(resdatetime: datetime, daynum: int):
    return resdatetime + timedelta(days=daynum)


# 获取当前时间的 daynum 天“前”的时间
def days_before_time(resdatetime: datetime, daynum: int):
    return resdatetime - timedelta(days=daynum)


# 获取某年某月的“第一天”日期
def get_firstday_of_month(year: int, mon: int):
    return date(year, mon, 1)


# 获取时间差
def get_datetime_between(d1: datetime, d2: datetime):
    if d1 > d2:
        b = d1 - d2
    else:
        b = d2 - d1
    if b.days == 0:
        return get_lessaday_str_of_timedelta(b)
    return str(b.days) + "天" + get_lessaday_str_of_timedelta(b)


# 获取时间差
# 返回 天数 ：int
def get_date_between(d1: date, d2: date):
    if d1 > d2:
        b = d1 - d2
    else:
        b = d2 - d1
    return b.days


# 获取 小于1天的 str
# 输入 timedelta
def get_lessaday_str_of_timedelta(res: timedelta):
    if (res.seconds / 3600) < 1:
        return str((int)(res.seconds / 60)) + "分" + str(res.seconds % 60) + "秒"
    else:
        return str((int)(res.seconds / 3600)) + "时" + str((int)(res.seconds % 3600 / 60)) + "分" + str(
            res.seconds % 60) + "秒"


# 获取某年某月的天数
def get_days_of_month(year: int, mon: int):
    return calendar.monthrange(year, mon)[1]


# str 转 数据库时间 datetime
def str_to_datetime(str):
    try:
        if ':' in str:
            return datetime.strptime(str, format_ymdhms)
        return datetime.strptime(str, format_ymd)
    except:
        return None


# str 转 数据库时间 date
def str_to_date(str):
    try:
        if ':' in str:
            return datetime.strptime(str, format_ymdhms).date()
        return datetime.strptime(str, format_ymd).date()
    except:
        return None


# 获取当前时间的str[2018-12-11 11:12:12 ] 数据库时间datetime
def get_datenow_str_ymdhms():
    return time.strftime(format_ymdhms, time.localtime())


# 获取当前时间的str[2018-12-11] 数据库时间date
def get_datenow_str_ymd():
    return time.strftime(format_ymd, time.localtime())


# 获取当前时间的str[20181211111212 ]
def get_datenow_str_ymdhms_():
    return time.strftime(format_ymdhms_, time.localtime())


# 获取当前时间戳[1545456565611]
def get_datenow_millis_str():
    return str(((int)(time.mktime(time.localtime()))))


# 获取时间格式 2018-12-11 11:12:11
# 传入日期格式：[2018-12-11 11:12  2018-12-11  1545656145.1545]
def get_date_str_ymdhms(dateRes):
    try:
        if isinstance(dateRes, float) | isinstance(dateRes, int):
            return time.strftime(format_ymdhms, time.localtime(dateRes))
        elif isinstance(dateRes, str):
            return time.strftime(format_ymdhms, time.strptime(dateRes, format_ymd))
        else:
            return '时间转换错误'
    except (TypeError, ValueError):
        return '时间转换错误TypeError，ValueError'


# 传入日期格式：[2018-12-11 11:12:12  1545656145.1545]
def get_date_str_ymd(dateRes):
    try:
        if isinstance(dateRes, float) | isinstance(dateRes, int):
            return time.strftime(format_ymd, time.localtime(dateRes))
        elif isinstance(dateRes, str):
            return time.strftime(format_ymd, time.strptime(dateRes, format_ymdhms))
        else:
            return '时间转换错误'
    except (TypeError, ValueError):
        return '时间转换错误TypeError，ValueError'


# 传入日期格式：[2018-12-11 11:12:12  1545656145.1545]
def get_date_str_ymdhm(dateRes):
    try:
        if isinstance(dateRes, float) | isinstance(dateRes, int):
            return time.strftime(format_ymdhm, time.localtime(dateRes))
        elif isinstance(dateRes, str):
            return time.strftime(format_ymdhm, time.strptime(dateRes, format_ymdhms))
        else:
            return '时间转换错误'
    except (TypeError, ValueError):
        return '时间转换错误TypeError，ValueError'


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


def is_valid_date(strdate):
    try:
        if ":" in strdate:
            time.strptime(strdate, "%Y-%m-%d %H:%M:%S")
        else:
            time.strptime(strdate, "%Y-%m-%d")
        return True
    except:
        return False
