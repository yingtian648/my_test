#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/9/26 10:03
# Author : LiuShiHua
# Desc :
from flask import Blueprint
from common.make_api_response import make_api_respone

from common.install_config import application, socketio
from common.print_req_rep import before_request, after_request
from module.jpush import push_util

IMAGE_URL = '/module/image'

img = Blueprint('images', __name__)

before_request

#
@application.route('/img/getImages', methods=['GET'])
def get_images():
    return make_api_respone(1, "请求成功", None, None)
