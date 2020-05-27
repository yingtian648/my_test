#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/10/8 14:46
# Author : LiuShiHua
# Desc :

import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

ettda_url = 'http://www.ettda.com'
ettda_url_login = 'http://maintenance.ettda.com/#/login'


class EttdaWeb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()  #窗口最大化
        self.driver.implicitly_wait(30)  # 隐性等待30秒
        self.driver.get(ettda_url_login)

    def test_ettda(self):
        inputs = self.driver.find_elements_by_class_name("el-input__inner")
        inputs[0].send_keys("13541354186")
        time.sleep(1.2)
        inputs[1].send_keys("00000000")
        time.sleep(1.2)
        self.driver.find_element_by_class_name("login-btn").click()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()  # 退出浏览器
