#coding = utf-8
import ddt
import unittest
import sys
from selenium.webdriver.android.webdriver import WebDriver
sys.path.append(r'D:\selenium_lianxi_demo')#添加当前工程目录
from business.register_business import RegisterBusiness
from selenium import webdriver
import os
import time
import HTMLTestRunnerNew

'''
ddt数据驱动与first_case.py结合,并且数据驱动生成测试报告,新的unittest加载方式
'''
@ddt.ddt
class SecondDdtCase(unittest.TestCase):
    img_file = 'D:/selenium_lianxi_demo/TestReport_Image/images/'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    @property
    def getImage(self):                                                             #查看@property的使用.doc文档，输出（'screenshot:', timestrmap, '.png'）给htmltestrunner方法遍历查找文件，赋值到htmltestrunner的src变量中
        '''
        截取图片,并保存在images文件夹
        :return: 无
        '''
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join(self.img_file, '%s.png' % str(timestrmap))
        self.driver.save_screenshot(imgPath)
        print  ('screenshot:', timestrmap, '.png')
        
    @getImage.setter
    def getImage(self):
        self.getImage                           #调用上面的getImage(self)，因为加了@property，所以它变成了变量，直接调用变量，不用加()
 
    def tearDown(self):
        self.getImage
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
    suite = unittest.TestLoader().loadTestsFromTestCase(SecondDdtCase) #以类加载测试用例
    '''
    一：unittest.TestLoader().loadTestsFromTestCase(类名)
    二：unittest.TestLoader().loadTestsFromMoudule(模块名)但是我看源码提示是说在3.5已经移除使用，那就不用这个了
    三：unittest.TestLoader().loadTestsFromName(方法名)
    四：unittest.TestLoader().loadTestsFromNames(方法名，复数形式)
    '''
    # suite.addTest(Sixth('test_login_email_error'))
    # suite.addTest(Sixth('test_login_name_error'))
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    filename = 'D:/selenium_lianxi_demo/TestReport_Image/'+timestr+'.html'
    print (filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=fp,title='测试结果如下：',description='用例执行情况：',tester='GGW')
    runner.run(suite)