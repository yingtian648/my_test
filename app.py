import asyncio
import threading

import sched

import websockets

from common.install_config import config, application, socketio
from common.timer_config import send_maintenance_msg, send_maintenance_msg1
from module.service.image.api_img import img, IMAGE_URL
from flask import Flask, render_template
from flask_socketio import SocketIO
from datetime import date
import datetime

from module.service.web_socket.api_socket import socket_time


def install_config():
    """
    加载config文件
     schedule.add_job(func=sync_ev_health, trigger='cron', month='*', day='*', hour='1', id='job5')
    schedule.add_job(func=sync_maintain_date, trigger='interval', seconds=3600, id='job6')
    :return:
    """
    pass

def install_socket():
    """
    加载config文件
    启动socket
    :return:
    """
    pass


def printHello():
    print("------" + str(datetime.datetime.now()) + "------")
    timer = threading.Timer(5, printHello)
    timer.start()

if __name__ == "__main__":
    mq_thr = threading.Thread(target=install_config, name='MQThread')
    mq_thr.daemon = True
    mq_thr.start()

    sq_thr = threading.Thread(target=install_socket, name='SOCKETThread')
    sq_thr.daemon = True
    sq_thr.start()

    application.register_blueprint(img, url_prefix=IMAGE_URL)

    # application.run(
    #     host=config.listen,
    #     port=config.port,
    #     debug=config.debug,
    #     threaded=True
    # )

    socketio.run(application)
