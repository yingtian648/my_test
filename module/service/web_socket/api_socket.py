#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2019/3/14 10:51
# Author : LiuShiHua
# Desc :

import asyncio
import datetime
import random
import websockets

async def socket_time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(socket_time, '172.16.2.74', 5577)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
