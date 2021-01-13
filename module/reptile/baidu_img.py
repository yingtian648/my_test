#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/9/25 17:07
# Author : LiuShiHua
# Desc : 百度图片爬虫

from urllib import parse
from urllib.request import *
from os.path import exists, join
from os import makedirs

import re
from common.init_config import base_image_path
import time
from util.date_format import get_datenow_millis_str

baidu_img_url = "http://image.baidu.com/"
search_url = baidu_img_url + '/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq={}_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd={}%5E00_1583X748&word={}'
load_more = baidu_img_url + '/search/flip?tn=baiduimage&ie=utf-8&word={}&pn={}&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0'

url_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
url_referer = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E7%BE%8E%E6%99%AF&ct=201326592&ic=0&lm=-1&width=&height=&v=flip'
header = {'User-Agent': url_agent, 'Referer': url_referer}


def search_img(key):
    input_key = key
    if key == None:
        input_key = input('请输入搜索【baidu图片】的关键字:')
    has_more = make_req_url_to_download(input_key, True, None)
    is_need_more = True
    is_search_more_first = True
    index_ = 20
    if not has_more:  # 没有更多了 直接退出
        print("Exit")
        return
    while is_need_more:
        input_is = input('是否搜索更多？(1搜索更多，其他任意键+回车退出)：')
        is_need_more = (input_is == '1')
        if not is_need_more:
            print("Exit")
            return
        if is_search_more_first:
            is_search_more_first = False
            index_ = 20
        else:
            index_ += 20
        has_more = make_req_url_to_download(input_key, False, index_)
        if not has_more:  # 没有更多了 直接退出
            print("Exit")
            return


def make_req_url_to_download(input_key, isFirst: bool, index_: int):
    input_key = parse.quote(input_key)  # 将文字编码  str3 = parse.unquote(str2) #解码字符串
    date_strap = get_datenow_millis_str() + "123"
    if isFirst:
        url = search_url.format(date_strap, date_strap, input_key)
    else:
        url = load_more.format(input_key, index_)
    print('----------------解析地址-----------------')
    print(url)
    req = Request(url, None, header)
    html = urlopen(req).read().decode('utf-8')  # 获取数据并解码
    # .*? 懒匹配
    urls = re.findall(r'"objURL":"(.*?)"', html)
    print('--------------解析后的数据---------------')
    print(urls)
    if len(urls) == 0:
        return False

    input_key = parse.unquote(input_key)  # 解码字符串
    download_img(urls, input_key)  # 下载图片
    return True


def download_img(imag_res_urls, name: str):
    if not exists(base_image_path):
        makedirs(base_image_path)
    index = 0
    for url in imag_res_urls:
        try:
            print("downloading....%s....%d" % (name, index))
            file_name = None
            if re.search('.jpg$', url) or re.search('.jpeg$', url):
                file_name = ("%s_" + str(index) + '_' + get_datenow_millis_str() + ".jpg") % name
            elif re.search('.png$', url):
                file_name = ("%s_" + str(index) + '_' + get_datenow_millis_str() + ".png") % name
            elif re.search('.gif$', url):
                file_name = ("%s_" + str(index) + '_' + get_datenow_millis_str() + ".gif") % name
            elif re.search('.bmp$', url):
                file_name = ("%s_" + str(index) + '_' + get_datenow_millis_str() + ".bmp") % name
            elif re.search('.webp$', url):
                file_name = ("%s_" + str(index) + '_' + get_datenow_millis_str() + ".webp") % name
            else:
                file_name = ("%s_" + get_datenow_millis_str() + '_' + str(index) + ".jpg") % name
            file_path = join(base_image_path, file_name)  # 存放下载图片的路径；E:\\picture是我本地存放路径
            urlretrieve(url, file_path)
            index += 1
        except Exception:
            print("downloaderror")


if __name__ == '__main__':
    search_img('美景')
