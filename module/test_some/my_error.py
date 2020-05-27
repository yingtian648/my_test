#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/10/19 13:54
# Author : LiuShiHua
# Desc :
import traceback


class BaseError(Exception):
    def __init__(self):
        self.err_msg = ''
        self.err_msg_detail = ''


class RequestParamsError(BaseError):
    def __init__(self, err_msg):
        self.err_msg = {'code': 70011, 'message': '请求参数错误'}
        self.err_msg_detail = "请求参数错误" + err_msg
        Exception.__init__(self, self.err_msg, self.err_msg_detail)

def alarm_note(ev_id):
    import requests,json
    try:
        touch_url = 'http://v3.hz.2012iot.com/api-chengdu-big-data-hz/triggerAlarmTips?evId=' + str(ev_id)
        touch_res = requests.get(touch_url)
        print(touch_res)
        print(json.loads(touch_res.text))
    except:
        print('报警触发事件1:发生异常' + str(traceback.format_exc()))

def try_test():
    x = "yuihdjs"
    try:
        y = int(x)
    except Exception as ep:
        raise RequestParamsError(str(ep))


if __name__ == "__main__":
    # try:
    #     try_test()
    # except BaseError as err:  # 当抛出的异常是“自定义异常”时执行此语句
    #     print(err.err_msg['message'])
    #     print(err.err_msg_detail)
    #     print(str(traceback.format_exc()))  # 打印错误发生点
    # except Exception as ep:  # 当抛出的异常是“非自定义异常”时执行此语句
    #     print(str(ep))
    #     print(str(traceback.format_exc()))
    alarm_note('102462263545124686')
