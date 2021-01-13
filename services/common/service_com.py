from flask import Blueprint

from common.init_config import application
from common.make_api_response import make_api_respone

from common.print_req_rep import before_request
from services.common import control_com

# 注册蓝图参数
module_common = Blueprint('module_common', __name__)
module_common_prefix = '/common'  # 前缀

before_request

@application.route(module_common_prefix + '/login', methods=['POST'])
def login():
    return make_api_respone(0,"success",control_com.login(),None)