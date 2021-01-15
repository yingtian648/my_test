#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/27 17:23
# Author : LiuShiHua
# Desc :

from module.api_test.util.file_util import change_dir_to_case
import os
import logging


# 打印日志 输出到文档
def logd(msg: str, parent_dir=None):
    if msg is None:
        return
    logging.debug(msg)
    write_into_file("DEBUG " + msg)


def logi(msg: str, parent_dir=None):
    if msg is None:
        return
    logging.info(msg)
    write_into_file("INFO " + msg)


def loge(msg: str, parent_dir=None):
    if msg is None:
        return
    logging.error(msg)
    write_into_file("ERROR " + msg)


# 写入文档
def write_into_file(msg: str, parent_dir=None):
    if parent_dir is None:
        file = open("running_log.txt", "a", encoding='utf-8', errors='ignore')
        file.write(msg + "\n")
        file.close()
    else:
        change_dir_to_case()
        os.chdir(parent_dir)
        file = open("running_log.txt", "a", encoding='utf-8', errors='ignore')
        file.write(msg + "\n")
        file.close()
        change_dir_to_case()

# 获取配置对应的日志级别
def get_log_level(log_level):
    if (log_level == "DEBUG"):
        return logging.DEBUG
    elif (log_level == "INFO"):
        return logging.ERROR
    elif (log_level == "DEBUG"):
        return logging.ERROR
    else:
        return logging.DEBUG
