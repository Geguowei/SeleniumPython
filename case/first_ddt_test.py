#coding = utf-8
import ddt
import unittest
import sys
from selenium.webdriver.android.webdriver import WebDriver
sys.path.append(r'D:\selenium_lianxi_demo')#添加当前工程目录
from business.register_business import RegisterBusiness
from selenium import webdriver
'''
ddt数据驱动与first_case.py结合,register_business.py文件增加def register_function方法
'''
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        self.driver.close()
        
    #邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息
    @ddt.data(
        ["12","GGW001","111111","code","user_email_erro","请输入有效的电子邮件地址"],
        ["@qq.com","GGW001","111111","code","user_email_erro","请输入有效的电子邮件地址"],
        ["12@qq.com","GGW001","111111","code","user_email_erro","请输入有效的电子邮件地址"]

    )
    
    @ddt.unpack
    def test_login_email_error(self,email,username,password,code,assertCode,assertText):
        email_erro = self.login.register_function(email,username,password,code,assertCode,assertText)
        return self.assertTrue(email_erro,'邮箱错误')
        
if __name__ == "__main__":
    unittest.main()
    