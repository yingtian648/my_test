#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/9/26 10:07
# Author : LiuShiHua
# Desc :
from flask import request

from common.init_config import application


@application.before_request
def before_request():
    print('================ 请求 ===============')
    print(str(request.headers).rstrip())
    print("请求地址：", str(request.path))
    print("请求方法：", str(request.method))
    print("请求ARGS参数：", str(request.args))
    print("请求FORM参数：", str(request.form))
    print("请求JSON参数：", str(request.get_json()))
    if (len(request.files) > 0):
        print("请求上传文件数量：", len(request.files.getlist("files")))


@application.after_request
def after_request(response):
    print('================ 返回 ===============')
    print("返回状态码：" + str(response.status_code).rstrip())
    print(str(response.headers).rstrip())
    try:
        print(str(response.data.rstrip()))  # 返回为文件时报错
    except:
        print("response file")
    return response
