from flask import Blueprint

from common.init_config import application
from common.make_api_response import make_api_respone

# 注册蓝图参数
module_file = Blueprint('module_file', __name__)
module_file_prefix = '/file'  # 前缀


@application.route(module_file_prefix + '/uploadFiles', methods=['GET'])
def uploadFiles():
    return make_api_respone(1, "请求成功", {'res': '111'}, None)
