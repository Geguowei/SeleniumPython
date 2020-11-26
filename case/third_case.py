#coding=utf-8
'''
HTMLTestRunnerNew生成测试报告,HTMLTestRunnerNew.py文件放到Python37\Lib\site-packages路径下，直接import引用
'''
import sys
from selenium.webdriver.android.webdriver import WebDriver
sys.path.append(r'D:\selenium_lianxi_demo')#添加当前工程目录
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunnerNew
import unittest
import os


class Third(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        self.driver.close()
        
    # def __init__(self):
    #     driver = webdriver.Chrome()
    #     driver.get('http://www.5itest.cn/register')
    #     driver.maximize_window()
    #     self.login= RegisterBusiness(driver)


    def test_login_email_error(self):
        email_erro = self.login.login_email_erro('34','user111','111111','1111')
        self.assertTrue(email_erro,'邮箱错误')
        
        # if email_erro==True:
        #     print('OK')
        # else:
        #     print('邮箱错误')
            
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

    def test_login_code_error(self):
        code_erro = self.login.login_code_erro('34','user111','111111','1111')
        self.assertTrue(code_erro,'验证码错误')

        # if code_erro==True:
        #     print('OK')
        # else:
        #     print('验证码错误')        

        #通过assert判断是否为error
        
    def test_login_success(self):
        success = self.login.user_base('34@qq.com','user111','111111','1111')
        TT = self.login.register_success()
        self.assertTrue(TT,'注册失败')

        # if self.login.register_success()==True:
        #     print('注册成功')
        # else:
        #     print('注册失败')
               
if __name__ == '__main__':
    file_path=os.path.join(os.getcwd()+"/report/"+"first_case.html")   #报告的路径拼接
    f = open(file_path,'wb')                                           #用读写的方式打开测试报告
    suite = unittest.TestSuite()
    suite.addTest(Third('test_login_code_error'))
    # suite.addTest(Third('test_login_password_error'))
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f,title='测试结果如下：',description='用例执行情况：',tester='GGW') #HTMLTestRunnerNew.HTMLTestRunner（stream=报告的读写方式流变量名,title='测试标题',description='用例执行情况描述：',tester='测试人员'）
    runner.run(suite)

            