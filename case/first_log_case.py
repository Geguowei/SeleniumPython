#coding=utf-8
'''
PO模型加日志运行
'''
import sys
from selenium.webdriver.android.webdriver import WebDriver
sys.path.append(r'D:\selenium_lianxi_demo')#添加当前工程目录
from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import unittest

class FirstLogCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.logger.info('啊啊啊啊啊')
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.logger.info('This is Chrome')
        self.driver.maximize_window()
        self.login= RegisterBusiness(self.driver)


    def tearDown(self):
        self.driver.close()
        
    @classmethod    
    def tearDownClass(cls):
        cls.log.close_handle()

        
    # def __init__(self):
    #     driver = webdriver.Chrome()
    #     driver.get('http://www.5itest.cn/register')
    #     driver.maximize_window()
    #     self.login= RegisterBusiness(driver)

    # @unittest.skip('跳过')  
    def test_login_email_error(self):
        email_erro = self.login.login_email_erro('34','user111','111111','1111')
        self.assertTrue(email_erro,'邮箱错误')
        
        # if email_erro==True:
        #     print('OK')
        # else:
        #     print('邮箱错误')
            
    @unittest.skip('跳过')  
    def test_login_name_error(self):
        name_erro = self.login.login_name_erro('34','user111','111111','1111')
        self.assertTrue(name_erro,'用户名错误')

        # if name_erro==True:
        #     print('OK')
        # else:
        #     print('用户名错误')


        
    def test_login_password_error(self):
        password_erro = self.login.login_password_erro('34','user111','111111','1111')
        self.assertTrue(password_erro,'密码错误')

        # if password_erro==True:
        #     print('OK')
        # else:
        #     print('密码错误')

    @unittest.skip('跳过')  
    def test_login_code_error(self):
        code_erro = self.login.login_code_erro('34','user111','111111','1111')
        self.assertTrue(code_erro,'验证码错误')

        # if code_erro==True:
        #     print('OK')
        # else:
        #     print('验证码错误')        

        #通过assert判断是否为error
    @unittest.skip('跳过')  
    def test_login_success(self):
        success = self.login.user_base('34@qq.com','user111','111111','1111')
        TT = self.login.register_success()
        self.assertTrue(TT,'注册失败')

        # if self.login.register_success()==True:
        #     print('注册成功')
        # else:
        #     print('注册失败')
               
if __name__ == '__main__':
    unittest.main()

            