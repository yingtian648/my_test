#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2019/3/15 14:36
# Author : LiuShiHua
# Desc :

from flask import Flask
from flask_socketio import SocketIO,emit

app = Flask(__name__)

socketio = SocketIO()
socketio.init_app(app)

"""
对app进行一些路由设置
"""

"""
对socketio进行一些监听设置
"""

if __name__ == '__main__':
    socketio.run(app,debug=True,host='172.16.2.74',port=5577)
