#coding=utf-8
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\selenium_start')
from selenium import webdriver
import time
import random
from PIL import Image
from base.find_element import FindElement
from ShowapiRequest import ShowapiRequest
class RegisterFunction(object):
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)
    #获取driver并且打开url
    def get_driver(self,url,i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:

            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver
    #输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)
    
    #定位用户信息，获取element
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    #获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefghijklmn',8))
        return user_info

    #获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        img = im.crop((left,top,right,height))
        img.save(file_name)

    #解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/1274-2","160666","6c7249013e10412785d5bb98305832fe" )
        r.addFilePara("imgFile", file_name)
        res = r.post()
        text = res.json()['showapi_res_body']['texts']
        return text
        # r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
        # r.addBodyPara("typeId", "35")
        # r.addBodyPara("convert_to_jpg", "0")
        # r.addFilePara("image", file_name) #文件上传时设置
        # res = r.post()
        # print(res.text)
        # text = res.json()['showapi_res_body']['Result']
        # return text
        #"D:/selenium截图/imooc1.png"

    #判断验证码对错
    def YZM(self,file_name):
        b=True
        while b:
            time.sleep(2)
            a=self.code_online(file_name)
            print('a:'+str(a))
            time.sleep(2)
            self.get_user_element('code_text').clear()
            self.send_user_info('code_text', a)
            self.get_user_element('register_button').click()
            try:
                c=self.get_user_element('code_text_erro').is_displayed()
                print('c:'+str(c))
                if c:
                    self.get_user_element('code_image').click()
                    time.sleep(2)
                else:
                    b=False
            except:
                b=False
                break


                
    def main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info+"@163.com"
        file_name = "D:/selenium截图/imooc1.png"
        #code_text = self.code_online(file_name)
        
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name',user_name_info)
        self.send_user_info('password',"111111")
        self.YZM(file_name)
        self.driver.close()
        
        # self.send_user_info('code_text',"11111")
        # self.get_user_element('register_button').click()
        # code_error = self.get_user_element("code_text_error")
        # if code_error == None:
        #     print("注册成功")
        # else:
        #     self.driver.save_screenshot("E:/Teacher/Imooc/SeleniumPython/Image/codeerror.png")
        # time.sleep(5)
        # self.driver.close()
    
if __name__ == '__main__':
    # for i in range(3): #多浏览器跑case
        register_function = RegisterFunction('http://www.5itest.cn/register',1)
        register_function.main()