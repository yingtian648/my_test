#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/25 10:41
# Author : LiuShiHua
# Desc :

def is_positive_integer_num(num, flag: float = 0):
    """
    判断参数是大于flag的正整数
    :param num:int
    :param flag:默认是0
    :return:
    """
    if num is not None and isinstance(num, int) and num > flag:
        return True
    return False


def is_float_num(num, flag: float = 0):
    """
    判断参数是否为正整数 或 正float数
    :param num: int、float
    :param flag: int、float: =-1时判断为>=0,否则判断大于flag才返回True
    :return:
    """
    if num is not None and (isinstance(num, float) or isinstance(num, int)):
        if flag == -1:
            return num >= 0
        return num > flag
    return False
