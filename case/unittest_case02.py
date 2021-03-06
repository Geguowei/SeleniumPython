#coding=utf-8
'''
unittest融合到first_case.py中
'''
import sys
from selenium.webdriver.android.webdriver import WebDriver
sys.path.append(r'D:\selenium_lianxi_demo')#添加当前工程目录
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest


class FirstCase02(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login= RegisterBusiness(self.driver)
    
    def tearDown(self):
        self.driver.close()
        print('这个是case的后置条件')
    
    def test_login_email_error(self):
        email_erro = self.login.login_email_erro('34','user111','111111','1111')
        if email_erro==True:
            print('OK')
        else:
            print('邮箱错误')
            
        
    def test_login_name_error(self):
        name_erro = self.login.login_name_erro('34','user111','111111','1111')
        if name_erro==True:
            print('OK')
        else:
            print('用户名错误')


        
    def test_login_password_error(self):
        password_erro = self.login.login_password_erro('34','user111','111111','1111')
        if password_erro==True:
            print('OK')
        else:
            print('密码错误')

        
    def test_login_code_error(self):
        code_erro = self.login.login_code_erro('34','user111','111111','1111')
        if code_erro==True:
            print('OK')
        else:
            print('验证码错误')        

        #通过assert判断是否为error
        
    def test_login_success(self):
        success = self.login.user_base('34@qq.com','user111','111111','1111')
        if self.login.register_success()==True:
            print('注册成功')
        else:
            print('注册失败')

    
if __name__ == '__main__':
    unittest.main()


            