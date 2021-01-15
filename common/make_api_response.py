#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/9/26 10:18
# Author : LiuShiHua
# Desc :
from flask import jsonify


def make_api_respone(code: int, message: str, data: dict, token):
    """
    构造接口响应内容
    :rtype:
    :param code: 响应代码【1:成功，2:失败,3:登录失效】
    code值：1 返回成功 405 客户端请求中的方法被禁止，415 mediatype——ContentType错误
    :param message: 消息
    :param data:  返回内容
    :return: dict
    """

    return jsonify({
        'code': code,
        'msg': message if message else '',
        'obj': data if data else '{}',
        'tokenStr': token if token else None
    })


def make_api_respone_failed(msg=None):
    """
    构造接口响应内容
    :rtype:
    :param code: 响应代码【1:成功，2:失败,3:登录失效】
    code值：1 返回成功 405 客户端请求中的方法被禁止，415 mediatype——ContentType错误
    :param message: 消息
    :param data:  返回内容
    :return: dict
    """

    return make_api_respone(-1, msg if msg else 'failed!', {}, None)


def make_api_respone_success():
    """
    构造接口响应内容
    :rtype:
    :param code: 响应代码【1:成功，2:失败,3:登录失效】
    code值：1 返回成功 405 客户端请求中的方法被禁止，415 mediatype——ContentType错误
    :param message: 消息
    :param data:  返回内容
    :return: dict
    """

    return make_api_respone(0, "success!", {}, None)
