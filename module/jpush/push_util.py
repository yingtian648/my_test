#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2019/6/21 10:07
# Author : LiuShiHua
# Desc :
import jpush
from jpush import common

app_key = 'caebb9bccfddf8633e205e48'
master_secret = '01f6d7cf6d6a6624f48c54bf'

_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")


def push_all():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="!hello python jpush api")
    push.platform = jpush.all_
    try:
        response = push.send()
        print(response)
    except common.Unauthorized:
        print("common.Unauthorized")
        raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        print("common.APIConnectionException")
        raise common.APIConnectionException("conn")
    except common.JPushFailure:
        print("JPushFailure")
    except:
        print("Exception")


def notification():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.platform = jpush.all_
    ios = jpush.ios(alert="Hello, IOS JPush!", sound="a.caf", extras={'k1': 'v1'})
    android = jpush.android(alert="Hello, Android msg", priority=1, style=1, alert_type=1, big_text='jjjjjjjjjj',
                            extras={'k1': 'v1'})
    push.notification = jpush.notification(alert="Hello, JPush!", android=android, ios=ios)
    result = push.send()


def options():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="Hello, world!")
    push.platform = jpush.all_
    push.options = {"time_to_live": 86400, "sendno": 12345, "apns_production": True}
    push.send()


def push_users_msg():
    user_alias = ['13541354186']
    push = _jpush.create_push()
    alias1 = {"alias": user_alias}
    print(alias1)
    push.audience = jpush.audience(
        alias1
    )
    push.notification = jpush.notification(alert="Hello world with audience!")
    push.platform = jpush.all_
    print(push.payload)
    push.send()

def silent():
    push = _jpush.create_push()
    push.audience = jpush.all_
    ios_msg = jpush.ios(alert="Hello, IOS JPush!", badge="+1", extras={'k1': 'v1'}, sound_disable=True)
    android_msg = jpush.android(alert="Hello, android msg")
    push.notification = jpush.notification(alert="Hello, JPush!", android=android_msg, ios=ios_msg)
    push.platform = jpush.all_
    push.send()


def sms():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="a sms message from python jpush api")
    push.platform = jpush.all_
    push.smsmessage = jpush.smsmessage("a sms message from python jpush api", 0)
    print(push.payload)
    push.send()


def validate():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="Hello, world!")
    push.platform = jpush.all_
    push.send_validate()


# for i in range(2):
#     push_users_msg()
