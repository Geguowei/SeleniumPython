#coding=utf-8
from selenium import webdriver
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
from time import sleep
driver = webdriver.Chrome()
#浏览器初始化
def driver_init():
    driver.maximize_window()
    driver.get('http://www.5itest.cn/register')
    sleep(3)

#获取element值
def get_element(id):
    element =driver.find_element_by_id(id)
    return element

#获取随机数
def get_range_user():
    user_info= ''.join(random.sample('1234567abcdefg',5))
    return user_info

#截取图片
def get_code_image():
    driver.save_screenshot('D:/selenium截图/imooc.png')
    code_element=driver.find_element_by_id('getcode_num')
    # print(code_element.location)
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width']+left
    height = code_element.size['height']+top
    im = Image.open('D:/selenium截图/imooc.png')
    img = im.crop((left,top,right,height))
    img.save('D:/selenium截图/imooc1.png')
    
#分析图片提取验证玛
def code_online():
    r = ShowapiRequest("http://route.showapi.com/1274-2","160666","6c7249013e10412785d5bb98305832fe" )
    r.addFilePara("imgFile", "D:/selenium截图/imooc1.png")
    res = r.post()
    text = res.json()['showapi_res_body']['texts']
    return text

#判断验证码对错
def YZM():
    b=True
    while b:
        get_code_image()
        sleep(2)
        a=code_online()
        print('a:'+str(a))
        sleep(2)
        get_element('captcha_code').clear()
        get_element('captcha_code').send_keys(a)
        get_element('register-btn').click()
        c=get_element('captcha_code-error').is_displayed()
        print('c:'+str(c))
        if c:
            get_element('getcode_num').click()
            sleep(2)
        else:
            b=False
            
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+'@163.com'
    driver_init()
    get_element('register_email').send_keys(user_email)
    get_element('register_nickname').send_keys(user_name_info)
    get_element('register_password').send_keys('111111')
    # get_code_image()
    # text=code_online()
    # get_element('captcha_code').send_keys(text)
    YZM()
    sleep(2)
    driver.close()
    
    
run_main()