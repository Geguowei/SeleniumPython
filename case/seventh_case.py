#coding=utf-8
'''
teardown，根据系统运行有无异常，增加截图功能
'''
import sys
from selenium.webdriver.android.webdriver import WebDriver
sys.path.append(r'D:\selenium_lianxi_demo')#添加当前工程目录
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
import os


class Seventh(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:    #self._outcome.errors()捕获当前程序有无异常，如果有异常就执行下面的，如果有异常就执行下面的截图,此次用的是for循环来判断的
            if error:
                case_name = self._testMethodName            #self._testMethodName 自动获取测试的方法名
                file_path = os.path.join(os.getcwd()+"/TestReport_Image/images/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()                                 
        

    def test_login_email_error(self):
        email_erro = self.login.login_email_erro('34','user111','111111','1111')
        self.assertTrue(email_erro,'邮箱错误')
        
    def test_login_name_error(self):
        name_erro = self.login.login_name_erro('34','user111','111111','1111')
        self.assertTrue(name_erro,'用户名错误')
       
    def test_login_password_error(self):
        password_erro = self.login.login_password_erro('34','user111','111111','1111')
        self.assertTrue(password_erro,'密码错误')

    def test_login_code_error(self):
        code_erro = self.login.login_code_erro('34','user111','111111','1111')
        self.assertTrue(code_erro,'验证码错误')

    def test_login_success(self):
        success = self.login.user_base('34@qq.com','user111','111111','1111')
        TT = self.login.register_success()
        self.assertTrue(TT,'注册失败')

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(Seventh('test_login_email_error'))
    runner = unittest.TextTestRunner()
    runner.run(suit)


            