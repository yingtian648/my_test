from flask import Blueprint, request

from common.init_config import application
from common.make_api_response import make_api_respone, make_api_respone_failed

from common.print_req_rep import before_request
from services.common import c_com

# 注册蓝图参数
module_common = Blueprint('module_common', __name__)
module_common_prefix = '/common'  # 前缀

before_request

"""
request.form.get("key", type=str, default=None) 获取表单数据，
request.args.get("key") 获取get请求参数，
request.values.get("key") 获取所有参数。
"""

@application.route(module_common_prefix + '/login', methods=['POST'])
def login():
    user_name = request.form.get('userName')
    password = request.form.get('password')
    if(user_name is None or password is None):
        return make_api_respone_failed("param:userName or password is null")
    return make_api_respone(0,"success", c_com.login(), None)