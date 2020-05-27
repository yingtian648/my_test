#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/9/26 9:31
# Author : LiuShiHua
# Desc :

import os
from abc import ABCMeta

class ConfigBase(object, metaclass=ABCMeta):
    _section = 'main'

    def __init__(self):
        pass

    @property
    def section(self):
        """
        使用 property + setter 注解防止用户指定无效值
        :return:
        """
        return self._section

    @section.setter
    def section(self, value):
        if value:
            self._section = value
        else:
            raise ValueError("指定的 section 属性值无效。")

    def class_attrs(self):
        """
        返回构造方法 __init__ 中初始化的类属性
        :return:
        """
        return vars(self)


class ConfigParser(object):
    @staticmethod
    def load(filename: str, config_object: ConfigBase):
        from configparser import ConfigParser

        # TODO 配置文件与HappyConfigBase定义不一致时，抛出异常

        if not isinstance(config_object, ConfigBase):
            raise Exception('config_object 不是 ConfigBase 类的子类对象。')

        try:
            if not os.path.exists(filename):
                print("[Error] 配置文件 %s 不存在" % filename)
                exit(1)

            cfg = ConfigParser()
            cfg.read(filename)

            class_attrs = config_object.class_attrs()
            section = config_object.section

            for name, value in class_attrs.items():
                if name == '_section':
                    continue

                t = type(value)

                if t is str:
                    v = cfg.get(section, name)
                    exec("config_object.%s='%s'" % (name, v))
                elif t is int:
                    v = cfg.getint(section, name)
                    exec("config_object.%s=%d" % (name, v))
                elif t is bool:
                    v = cfg.getboolean(section, name)
                    exec("config_object.%s=%s" % (name, v))
                elif t is float:
                    print('float')
                    v = cfg.getfloat(section, name)
                    exec("config_object.%s=%f" % (name, v))
                else:
                    v = cfg.getboolean(section, name)
                    exec("config_object.%s=%s" % (name, v))
        except Exception as e:
            print("[Error] 配置文件读取错误：%s" % str(e))
            exit(1)