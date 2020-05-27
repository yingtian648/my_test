#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/9/26 10:27
# Author : LiuShiHua
# Desc :

from sqlalchemy.ext.declarative import declarative_base

MyReptileModel = declarative_base()

__all__ = [
    "MyReptileModel",
]