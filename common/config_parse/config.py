#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/9/26 9:30
# Author : LiuShiHua
# Desc :

from common.config_parse.parse_util import ConfigBase


class Config(ConfigBase):
    """
    配置文件模板
    """
    def __init__(self):
        super().__init__()

        self._section = 'my_reptile'
        self.listen = ''
        self.port = 0
        self.debug = True

        self.log_level = "DEBUG"

        self.mysql_host = ''
        self.mysql_port = 3306
        self.mysql_user = ''
        self.mysql_pwd = ''
        self.mysql_db = ''


        self.file_base_path = ''