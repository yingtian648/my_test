from flask import Blueprint, request

from common.init_config import application
from common.make_api_response import make_api_respone, make_api_respone_failed
from common.print_req_rep import before_request
from services.files import c_file

# 注册蓝图参数
module_file = Blueprint('module_file', __name__)
module_file_prefix = '/file'  # 前缀

before_request


@application.route(module_file_prefix + '/uploadFiles', methods=['POST'])
def uploadFiles():
    receive_files = request.files.getlist("files")
    if(receive_files is None or len(receive_files)==0):
        return make_api_respone_failed("param:files need")
    return c_file.uploadFiles(receive_files)


@application.route(module_file_prefix + '/downloadFile', methods=['GET'])
def downloadFile():
    file_name = request.args.get('file_name')
    if (file_name is None or str(file_name).isspace()):
        return make_api_respone_failed("param:file_name can not be null")
    return c_file.downloadFile(file_name)
