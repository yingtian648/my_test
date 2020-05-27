#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2019/8/8 16:44
# Author : LiuShiHua
# Desc :

import json
import paho.mqtt.client as mqtt
import time, datetime

HOST = 'elevator.mqtt.ettda.com'
PORT = 1873
USER_NAME = "mwteckiot"
USER_PWD = "Gn84cC@gd1yBUMvN3^"
# '#'号是通配符，匹配所有
# 消息服务质量,0最多一次，1最少一次，2只一次
subscribe_topic_running = "them/running/SNHSMAN19380918C"
subscribe_topic_command = "them/gsensor/#"
subscribe_topic_gsensor = "them/gsensor/#"
subscribe_them_all = "them/#"
# publish_topic = "them/command/SNE3975D298EAD94"
publish_topic = "them/command/SNQX0C63FC1CCB49"
CLIENT_ID = "11"


def on_connect(client, userdata, flags, rc):
    """
    链接mqtt成功、失败都会回调此函数
    :param client:
    :param userdata:
    :param flags:
    :param rc:0.成功 1.错误的协议版本 2.无效的 client ID  3.服务器不可用  4.错误的用户名或密码  5.无法验证
    :return:
    """
    print("Connected with result code " + str(rc))
    client.subscribe(subscribe_topic_running)  # 订阅消息


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(datetime.datetime.now()) + str(msg.payload.decode('utf-8')))


def on_running_message(client, userdata, msg):
    print(msg.topic + " " + str(datetime.datetime.now()) + str(msg.payload.decode('utf-8')))

def on_gsensor_message(client, userdata, msg):
    print(msg.topic + " " + str(datetime.datetime.now()) + str(msg.payload.decode('utf-8')))

def on_command_message(client, userdata, msg):
    print(msg.topic + " " + str(datetime.datetime.now()) + str(msg.payload.decode('utf-8')))


# 订阅回调
def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)


# 取消订阅回调
def on_unsubscribe(client, userdata, mid, granted_qos):
    print("On unSubscribed: qos = %d" % granted_qos)


# 发布消息回调
def on_publish(client, userdata, mid, granted_qos):
    print("On onPublish: qos = %d" % granted_qos)


# 断开链接回调
def on_disconnect(client, userdata, rc):
    print("Unexpected disconnection rc = " + rc)


data = {
    "cmd": "reboot_now",
    "ct": {
        "url": "http://mwteck-apk.oss-cn-shanghai.aliyuncs.com/apk/mix_device_20191122_1.0.16.apk?Expires\u003d1575873155\u0026OSSAccessKeyId\u003dLTAIZcN4S8ogkMrR\u0026Signature\u003dwr95NWDLXq4XISgtX7sj9iys%2BkQ%3D",
        "md": "XXX",
        "tp": "nano",
        "vs": "1.0.16",
        "tm": "1574401984",
        "uninstallFlag":1,
        "level":"3",
        "poff":"14:20",
        "pon":"14:40",
        "id": 382528847783923712
    }
}

param = json.dumps(data)
client = mqtt.Client(CLIENT_ID)
client.username_pw_set(USER_NAME, USER_PWD)
client.on_connect = on_connect
client.on_message = on_message
"""
 如果要用通配符同时处理多个话题的消息，例如用 sensors/# 匹配 sensors/temperature 和 sensors/humidity 话题，
 可以用 message_callback_add() 设置回调函数：（如下）
 
 如果同时设置了 on_message() 和 message_callback_add() 回调函数，会首先寻找合适的 message_callback_add() 
 定义的话题过滤器，如果没有匹配，才会调用 on_message()
"""
client.message_callback_add(subscribe_topic_running, on_running_message)
client.message_callback_add(subscribe_topic_command, on_command_message)
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
client.on_publish = on_publish
client.on_disconnect = on_disconnect
client.connect(HOST, PORT, 60)
client.publish(publish_topic, payload=param, qos=0)  # 发送消息
client.loop_forever()
