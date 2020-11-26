#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC #预期判断类库
from selenium.webdriver.support.wait import WebDriverWait #引用显示等待
from selenium.webdriver.common.by import By #定位方式
from time import sleep
import random #随机生成模块，比如随机生成注册用户名
from PIL import Image
from ShowapiRequest import ShowapiRequest
driver = webdriver.Chrome()
driver.get('http://www.5itest.cn/register')
sleep(4)
driver.maximize_window()
'''
Title = EC.title_contains('注册') #预判断tilte是否正确
print (Title(driver))             #返回True OR False

localted = (By.CLASS_NAME,'controls') #By定位元素需要引用相应类库
WebDriverWait(driver,10).until(EC.visibility_of_element_located(localted)) 


# WebDriverWait(@a,int).until(@b(@c))
# @a 浏览器
# int 等待的时间
# EC.visibility_of_element_located 检查元素是否存在以及元素是否可见
# @c 注意这边放定位元素时只能用by赋值的定位变量，driver.find_element...赋值的定位变量会报错。


email = driver.find_elements_by_class_name('form-control')[1]
print(email.get_attribute('placeholder')) #获取placeholder属性的提示信息
email_zidong = ''.join(random.sample('1234567abcdefg',5))+'163@qq.com'#自动生成注册邮箱名，需要先引用相应类库：生成源，生成几位数,且可以加格式
email.send_keys(email_zidong)
print(email.get_attribute('value'))#获取输入后的信息

# for i in range(5):
#     email_zidong= random.sample('1234567abcdefg',5)#这个打印的结果是个list
#     email_zidong= ''.join(random.sample('1234567abcdefg',5))+'163@qq.com'#这个打印的结果是个字符串并且可以加格式
#     print(email_zidong) 



username_element = driver.find_element_by_id('register_nickname')
username_element.send_keys('123')


password = driver.find_element_by_id('register_password')
password.send_keys('123')
yanzhen = driver.find_element_by_id('captcha_code')
yanzhen.send_keys('123')
click = driver.find_element_by_id('register-btn')
click.click()
'''
driver.save_screenshot('D:/selenium截图/imooc.png') #截图
code_element=driver.find_element_by_id('getcode_num')
print(code_element.location)#{x=12,y=34}，某个元素的位置
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open('D:/selenium截图/imooc.png')#打开之前截的图,需要先引用Image的类库，没有类库可以：pip install Pillow。安装后再引用
# im.resize((1920,1080),Image.BILINEAR)
img = im.crop((left,top,right,height))#在截图的基础上根据坐标抠出自己需要的图片
img.save('D:/selenium截图/imooc1.png')

r = ShowapiRequest("http://route.showapi.com/1274-2","160666","6c7249013e10412785d5bb98305832fe" )
r.addFilePara("imgFile", "D:/selenium截图/imooc1.png")
res = r.post()
text = res.json()['showapi_res_body']['texts']
print(text) # 返回信息
yanzhen = driver.find_element_by_id('captcha_code')
yanzhen.send_keys(text)
sleep(3)
driver.close()
