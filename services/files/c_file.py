from flask import send_file, send_from_directory
import os

from common.make_api_response import make_api_respone_failed, make_api_respone_success
from common.init_config import file_base_path

# os.path参考：https://www.runoob.com/python/python-os-path.html
from services.files.d_file import save_file_to_disk
from util.log_util import logd

BASE_LOCAL_PATH = file_base_path  # 本地路径


def downloadFile(file_name):
    """
    取本地文件来传给客户端
    :param file_name:
    :return:
    """
    dir = os.path.join(BASE_LOCAL_PATH, file_name)  # 将目录和文件名合成一个路径
    if (os.path.exists(dir)):
        return send_from_directory(BASE_LOCAL_PATH, file_name, as_attachment=True)  # 需要传入dir是os的dir  也可以用send_file
    return make_api_respone_failed("文件不存在")


def uploadFiles(receive_files):
    logd("come in to uploadFiles")
    for file in receive_files:
        save_file_to_disk(file)
    return make_api_respone_success()
