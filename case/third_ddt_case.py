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
from util.excel_util import ExcelUtil  #导入ExcelUtil类
ex = ExcelUtil()  #实例化导入的类
data = ex.get_data()

'''
xlrd读取xls文件，与测试用例，截图结合，以文件形式实现数据驱动'''
@ddt.ddt
class SecondDdtCase(unittest.TestCase):
    img_file = 'D:/selenium_lianxi_demo/TestReport_Image/images/'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    @property
    def getImage(self):                                                             
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
        self.getImage                           
 
    def tearDown(self):
        self.getImage
        self.driver.close()       
        
    #邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息
    '''
    #@ddt.data(存放的数据驱动具体数据)
    @ddt.data(
        ["12","GGW001","111111","code","user_email_erro","请输入有效的电子邮件地址"],
        ["@qq.com","GGW001","111111","code","user_email_erro","请输入有效的电子邮件地址"],
        ["12@qq.com","GGW001","111111","code","user_email_erro","请输入有效的电子邮件地址"]

    )
    @ddt.unpack    #把列表里的数据分开了
    '''
    @ddt.data(*data)   #加了*号和不加* 号的,*把列表里的数据分开了；可以简单理解为@ddt.data(*)=@ddt.unpack本质是由区别的，见杂记文档； 但是@ddt.data(*)这边的data为类上面的data，从ExcelUtil引进来的
    def test_login_email_error(self,data):
        email,username,password,code,assertCode,assertText = data   #此data同上，python，list的赋值方法，变量 = 列表
        email_erro = self.login.register_function(email,username,password,code,assertCode,assertText)
        return self.assertTrue(email_erro,'邮箱错误')
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SecondDdtCase) 
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    filename = 'D:/selenium_lianxi_demo/TestReport_Image/'+timestr+'.html'
    print (filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=fp,title='测试结果如下：',description='用例执行情况：',tester='GGW')
    runner.run(suite)