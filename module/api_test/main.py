#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/29 14:16
# Author : LiuShiHua
# Desc :


# 默认测试地址
from module.api_test.util.find_case_util import find_case_file_to_test

# BASE_URL = 'http://172.16.2.16:8001'
# BASE_URL = 'http://api.t4.2012iot.com'  # t4
# BASE_URL = 'http://api.t4.2012iot.com/api-python-wechat'  # t4
BASE_URL = 'http://v3m2.api.2012iot.com'  #正式
# 默认请求方法
BASE_METHOD = "GET"
# 默认请求成功后返回code
SUCCESS_CODE = 0

token = 'MjE5OTIwMzA4Mjk4MDk2NjQwX3Rva2VuXywsLDE1NDU3OTAwNDE1MjY='

pubid = 'oVIDC1KvbcEQzwwnQIE8S_SMlMrE'

# "Content-Type": "application/json"
BASE_HEADER = {
    # "tokenStr": token,
    "Authorization": token,
    "publicId": pubid
}

if __name__ == '__main__':
    find_case_file_to_test(BASE_URL, BASE_HEADER, BASE_METHOD)
