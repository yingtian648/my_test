#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/9/26 15:34
# Author : LiuShiHua
# Desc :
from urllib.request import *
import re
import os
from os import makedirs
from os.path import exists
import json

from common.install_config import base_songs_path

url_163_download = 'http://music.163.com/song/media/outer/url?id={}.mp3'

url_toplist = 'https://music.163.com/#/discover/toplist'
base_write_file = 'D:\\pythonfile\\test_file.txt'

url_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
url_referer = 'https://music.163.com/'
header = {'User-Agent': url_agent, 'Referer': url_referer}


def download_song(song_name, song_id):
    try:
        url = url_163_download.format(song_id)
        print("正在下载歌曲...{}".format(song_name))
        urlretrieve(url, base_songs_path + '\\{}.mp3'.format(song_name))
        print("下载成功")
    except Exception:
        print("download_song_error")


def get_163_songs_info():
    # url = 'https://music.163.com/discover/toplist'
    url = 'https://music.163.com/discover/toplist'
    req = Request(url, None, header)
    html = urlopen(req).read().decode()
    datas = re.findall(r'<textarea id="song-list-pre-data" style="display:none;">(.*?)</textarea>', html)
    print('--------------匹配----------')
    print(datas)
    real_data = str(datas[0])
    print('--------------写入----------')
    fd = os.open(base_write_file, os.O_RDWR | os.O_CREAT)
    os.write(fd, real_data.encode('utf-8'))
    os.close(fd)
    print('--------------json解析----------')
    real_data = json.loads(real_data)
    print(real_data)
    ind = 1
    for data in real_data:
        try:
            print("序号 " + str(ind) + "\tid = " + str(data['id']) + "\t\t歌曲:" + data['name'] + "   作者: " +
                  ((data["artists"])[0])['name'])
        except Exception:
            pass
        ind += 1
    return real_data


def lead_to_download(songs):
    print("下载路径：" + base_songs_path)
    if not exists(base_songs_path):
        makedirs(base_songs_path)
    is_need_download = True
    while is_need_download:
        song_index = input('请输入要下载的歌曲序号(0回车退出):')
        if not song_index.isdigit():
            print("请输入数字")
            continue
        song_index = int(song_index)
        if 0 == song_index:
            print('Exit')
            break
        if song_index > len(songs) or song_index < 1:
            print("歌曲序号错误")
        song = songs[song_index - 1]
        download_song(song['name'], song['id'])


if __name__ == '__main__':
    # songs = get_163_songs_info()
    # lead_to_download(songs)
    download_song("草原春天美", 1380849170)


