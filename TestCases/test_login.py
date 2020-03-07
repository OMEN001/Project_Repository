#_*_conding:utf-8_*_
#@Time    :2020/2/1017:41
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com
import unittest
import time
import ddt
import logging
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDatas import Common_Datas as CD
from TestDatas import login_datas as LD
from Common import logger

@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        #打开浏览器
        self.driver = webdriver.Chrome()
        #窗口最大化
        self.driver.maximize_window()
        #访问登录页面
        self.driver.get(CD.login_url)
        self.lp = LoginPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_success_login(self):
        logging.info("登录功能 - 正常场景用例：输入正确的用户名登录成功")
        #输入用户名登录
        self.lp.login(LD.success_data["username"],LD.success_data["passwd"])
        time.sleep(2)
        #url发生改变
        self.assertEqual(LD.success_data["check_url"],self.driver.current_url)
        #登录的用户是否存在
        self.assertTrue(HomePage(self.driver).user_is_existed())

    # def test_no_login(self):
    #     logging.info("登录功能 - 异常场景用例：输入不存在用户名登录失败")
    #     # 输入用户名登录
    #     self.lp.login(LD.no_exit_datas["username"], LD.no_exit_datas["passwd"])
    #     self.assertEqual(self.lp.no_exit_login(),LD.no_exit_datas["check"])
    #
    # def test_error_passwd_login(self):
    #     logging.info("登录功能 - 异常场景用例：输入错误的用户密码登录失败")
    #     self.lp.login(LD.passwd_error["username"], LD.passwd_error["passwd"])
    #     self.assertEqual(self.lp.no_exit_login(), LD.passwd_error["check"])
    #
    # @ddt.data(*LD.wrong_datas)
    # def test_login_failed_by_wrong_datas(self,case):
    #     # 步骤
    #     # 1、登陆页面 - 登陆操作
    #     self.lp.login(case["username"],case["passwd"])
    #     # 断言
    #     self.assertEqual(self.lp.get_error_msg_from_login_form(),case["check"])

