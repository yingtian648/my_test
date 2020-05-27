#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/9/26 9:43
# Author : LiuShiHua
# Desc :
from pathlib import PurePath
from socket import SocketIO

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS


from common.config_parse import *
CONFIG_DIR = PurePath(__file__).parent.parent / 'config'
CONFIG_FILENAME = str(CONFIG_DIR / 'common.ini')
config = Config()
ConfigParser.load(CONFIG_FILENAME, config)

base_image_path = config.save_image_path
base_video_path = config.save_video_path
base_songs_path = config.save_songs_path


# 为支持 uWSGI 默认加载点，Flask 应用名称不能修改
application = Flask('api-warp-drive')
# 支持 JSON 显示中文
application.config['JSON_AS_ASCII'] = False
application.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(application)

# 前端跨域
CORS(application)

DB_URI = 'mysql+pymysql://%s:%s@%s:%d/%s?charset=utf8' % (config.mysql_user,
                                                          config.mysql_pwd,
                                                          config.mysql_host,
                                                          config.mysql_port,
                                                          config.mysql_db)

engine = create_engine(DB_URI,
                       pool_size=100,
                       max_overflow=0,
                       pool_timeout=60,  # 超时时间
                       pool_pre_ping=True)  # 从连接池获取连接之前检查有效性

Session = sessionmaker(bind=engine)
db_session = Session()