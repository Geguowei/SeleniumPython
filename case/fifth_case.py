#coding=utf-8
'''
HTMLTestRunnerNew生成测试报告,测试报告和截图名字随机生成
'''
import sys
from selenium.webdriver.android.webdriver import WebDriver
sys.path.append(r'D:\selenium_lianxi_demo')#添加当前工程目录
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunnerNew
import unittest
import os
import time


class Fifth(unittest.TestCase):
    img_file = 'D:/selenium_lianxi_demo/TestReport_Image/images/'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)
        
    def screenshot(self):
        timestr=time.strftime('%Y%m%d_%H.%M.%S',time.localtime(time.time()))
        img_name=timestr+'.png'
        self.driver.get_screenshot_as_file('%s%s' % (self.img_file,img_name))
        return img_name

    def tearDown(self):
        self.screenshot()
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
    suite = unittest.TestSuite()
    suite.addTest(Fifth('test_login_code_error'))
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    filename = 'D:/selenium_lianxi_demo/TestReport_Image/'+timestr+'.html'
    print (filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=fp,title='测试结果如下：',description='用例执行情况：',tester='GGW')
    runner.run(suite)
            