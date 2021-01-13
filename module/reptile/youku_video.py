#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/9/29 13:53
# Author : LiuShiHua
# Desc :
import random
from urllib.request import *
import re
import os
from os import makedirs
from os.path import exists
import json
import datetime
# import rsa
import sys
import base64

from common.init_config import base_video_path
from util.date_format import get_date_between
import cProfile

RANDOM_09AZ = ("0123456789abcdefghijklmnopqrstuvwxyz")

format_ymdhms = "%Y-%m-%d %H:%M:%S"
format_ymdhm = "%Y-%m-%d %H:%M"
format_ymd = "%Y-%m-%d"

video_play_url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1537867870067_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%BE%8E%E6%99%AF'

url_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
url_referer = video_play_url
header = {'User-Agent': url_agent, 'Referer': url_referer}

message = "ni_hao_wo_de_zu_guo"

pub_key = '-----BEGIN RSA PUBLIC KEY-----\nMIGJAoGBAIsdz29RRLO3zKsl8PHJDl3UBOik6Yps8sfVFTkCavZoK1dPbsX7Z4af9Ej0fRwbJ932jZetEhDcrldo0Y3V8X1XgmxeUmR6+IvOf8oeKouK6v+Ju1QHKQBRZ7E2Kx+C5MQxsZXInhRaCA8K7wrUhtzBzZ1jnBwrR885fMGgULslAgMBAAE=\n-----END RSA PUBLIC KEY-----'
priv_key = '-----BEGIN RSA PRIVATE KEY-----\nMIICYAIBAAKBgQCLHc9vUUSzt8yrJfDxyQ5d1ATopOmKbPLH1RU5Amr2aCtXT27F+2eGn/RI9H0cGyfd9o2XrRIQ3K5XaNGN1fF9V4JsXlJkeviLzn/KHiqLiur/ibtUBykAUWexNisfguTEMbGVyJ4UWggPCu8K1Ibcwc2dY5wcK0fPOXzBoFC7JQIDAQABAoGAZXWfVOtrdLsm7Oel+2EMNkgsMFQd85QT2MRCTyrBQealPW80NfZuAZRlAFQ3bqkrgUmQ6L8TvvKDwEI0fJcc39/ciGXVIu5rwkWARuD9JKMg07mfa+YyA28B2UYx7wnP0l5CHFXmwmWtPk5fmXjnXDIMm3+6xaJnX/M2MuGAq8ECRQDZNm8q+TsysjOJfLbgyO4+ydybGjnPm0U6K4jaHItHaBpV6geRHikNfndgfA+Moup2LW7W0Bnmz22LVAbjcegY1GBHdQI9AKP1UfpCI7QnEFj8Oi6KG5huGVD35gZVRRXMqCEeJ8ggTDvxXhUcRmz4On3OzVX/IRMx21syEYOQBB7e8QJEM7oh2TMHJPiJC2nWx0syaWN7FLi3IbiRUNwDOCXqCTRCaUlVSfrLvfnrBeAld9FoUoJZTfC66ltlc/OrvEhpBFi3IO0CPB7mOdffJRlrj0Il7tUchAzbGvxOa9Rft5BfLIRpSXgG1jcpyuBRntgkg+l30uzVEyep6rwqGHDh8FTdEQJFALqx+WHGimgrMtYPV/FH1CTxtxKb9v2YNPkx9YIDuxkwLh+beUzmHWRQqkCErEx7ln0Dn2mWSsOLAvGwGdSMhyfmqDkq\n-----END RSA PRIVATE KEY-----'


# # 加密
# def msg_encrypt(msg: str):
#     print('------------加密-----------')
#     pub = rsa.PublicKey.load_pkcs1(pub_key.encode('utf-8'))
#     print(type(pub))
#     secret_msg = rsa.encrypt(msg.encode('utf-8'), pub)
#     print(secret_msg)
#     return secret_msg
#
#
# # 解密
# def msg_dencrypt(secret_msg: str):
#     print('------------解密-----------')
#     priv = rsa.PrivateKey.load_pkcs1(priv_key.encode('utf-8'))
#     print(type(priv))
#     res_msg = rsa.decrypt(secret_msg, priv)
#     print(res_msg.decode('utf-8'))
#     return
#
#
# def ras_install():
#     (pubkey, privkey) = rsa.newkeys(1024)
#     pub = pubkey.save_pkcs1()
#     priv = privkey.save_pkcs1()
#     print(pub.decode('utf-8'))
#     print(priv.decode('utf-8'))
#     return


def logging(fun):
    def decorated(*args, **kwargs):
        print("enter_func:" + str(fun.__name__))
        print("params：" + str(args) + str(kwargs))
        return fun(*args, **kwargs)

    return decorated


def func_performance_log(fun):
    # fun_str = str(fun.__name__) + "(" + str(fun.__args__) + ")"
    # cProfile.run(fun_str)

    def decorated(*args, **kwargs):
        fun_str = str(fun.__name__) + "(" + str(args) + ")"
        cProfile.run(fun_str)
        print(fun_str)
        result = fun(*args, **kwargs)
        print(str(result))
        cProfile.run(str(result))
        print(result)
        return None

    return decorated


def func_performance_log1(fun):
    import time
    """
    测试代码块所用时间
    :param fun:
    :return:
    """
    def wrapper(*args, **kwargs):
        print("enter_func:" + str(fun.__name__))
        print("params：" + str(args) + str(kwargs))
        t1 = time.time()
        result = fun(*args, **kwargs)
        t2 = time.time()
        print("[" + fun.__name__ + "]运行时长:" + str(t2 - t1))
        return result
    return wrapper


# 判断时间格式 是否是datetime str
@func_performance_log1
def is_datatime_str(res_str):
    print("进入函数")
    try:
        for i in range(10000):
            i += i
        print(i)
        print(datetime.strptime(res_str, format_ymdhms).date())
        return True
    except Exception:
        return False


# 判断时间格式 是否是date str
def is_data_str(res_str):
    try:
        print(datetime.strptime(str, format_ymd).date())
        return True
    except Exception:
        return False


if __name__ == '__main__':
    is_datatime_str('2018-12-12')
    # cProfile.run("is_data_str('2018-12-12 21')")
    for i in range(10):
        print(i)
