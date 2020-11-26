#coding=utf-8
'''
截图总结:
1.find_element.py的截图是截取定位元素错误时的截图；截图路劲在D:/selenium_lianxi_demo/Image/；命名方式是定位元素属性值.png；
2.teardown里面的截图，是捕获当前程序有无异常，有异常就截图；截图路径存放在D:/selenium_lianxi_demo/TestReport_Image/images/；命名方式是测试用例名称；这个截图暂定是不和测试报告结合的，要是结合也可实现
3.teardown里面的截图，是必执行的；截图路径存放在D:/selenium_lianxi_demo/TestReport_Image/images/；命名方式是'%Y%m%d_%H.%M.%S.png;这个截图是与测试报告结合的，还可根据实际需要与断言结合运行
！！！此文件是将2，3结合，并将3进行了改良，具体既然图逻辑如下：
1）当前程序有异常时，截图，存放在D:/selenium_lianxi_demo/TestReport_Image/images/；命名方式是测试用例名称；
2）assert断言错误时，截图，存放在D:/selenium_lianxi_demo/TestReport_Image/images/；命名方式是'%Y%m%d_%H.%M.%S.png,此测试用例为失败，并且与测试报告结合
因为此测试用例程序异常和assert断言错误并无具体区分，所以在此测试用例中无感，感觉这两个一样


!!!!试验失败，assert断言错误时，截图，并且与测试报告结合；思考再三可以在register_business里面进行断言截图，执行run这边还没想到好的解决方案
'''
import sys
from selenium.webdriver.android.webdriver import WebDriver
sys.path.append(r'D:\selenium_lianxi_demo')#添加当前工程目录
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
import os
import HTMLTestRunnerNew



class Seventh(unittest.TestCase):
    img_file = 'D:/selenium_lianxi_demo/TestReport_Image/images/'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)
        
    @property
    def getImage(self):                                                        #查看@property的使用.doc文档，输出（'screenshot:', timestrmap, '.png'）给htmltestrunner方法遍历查找文件，赋值到htmltestrunner的src变量中
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
        if False:
            self.getImage                       #此截图为assert判断结果截图，并且记录到测试报告中
        time.sleep(2)
        for method_name,error in self._outcome.errors:    #此截图为捕获异常截图，不记录到测试报告中，要是想记录到测试报告中，将命名方式改为与 @property的def getImage命名一致就可以
            if error:
                case_name = self._testMethodName            #self._testMethodName 自动获取测试的方法名
                file_path = os.path.join(os.getcwd()+"/TestReport_Image/images/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()                                 
        


        
    def test_login_email_error(self):
        email_erro = self.login.login_email_erro('34','user111','111111','1111')
        self.assertTrue(email_erro,'邮箱错误')
        
    def test_login_code_error(self):
        code_erro = self.login.login_code_erro('34','user111','111111','1111')
        self.assertTrue(code_erro,'验证码错误')
    
    # def test_login_name_error(self):
    #     name_erro = self.login.login_name_erro('34','》》','111111','1111')
    #     self.assertTrue(name_erro,'用户名错误')
       
    # def test_login_password_error(self):
    #     password_erro = self.login.login_password_erro('34','user111','111111','1111')
    #     self.assertTrue(password_erro,'密码错误')

    # def test_login_code_error(self):
    #     code_erro = self.login.login_code_erro('34','user111','111111','1111')
    #     self.assertTrue(code_erro,'验证码错误')

    # def test_login_success(self):
    #     success = self.login.user_base('34@qq.com','user111','111111','1111')
    #     TT = self.login.register_success()
    #     self.assertTrue(TT,'注册失败')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Seventh('test_login_email_error'))
    # suite.addTest(Seventh('test_login_code_error'))
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    filename = 'D:/selenium_lianxi_demo/TestReport_Image/'+timestr+'.html'
    print (filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=fp,title='测试结果如下：',description='用例执行情况：',tester='GGW')
    runner.run(suite)
            

            