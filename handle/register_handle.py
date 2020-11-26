#coding=utf-8
from page.register_page import RegisterPage
class RegisterHandle(object):
    def __init__(self,driver):
        self.register_p = RegisterPage(driver)
    #输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)

    #输入用户名
    def send_user_name(self,username):
        self.register_p.get_username_element().send_keys(username)
    
    #输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)
    
    #输入验证码
    def send_user_code(self,code):
        self.register_p.get_code_element().send_keys(code)
    
    #获取文字信息
    def get_user_text(self,info,user_info):
        try:
            if info == 'user_email_erro':
                text = self.register_p.get_email_erro_element().text
            elif info == 'user_name_erro':
                text = self.register_p.get_username_erro_element().text
            elif info == 'password_erro':
                text = self.register_p.get_password_erro_element().text
            else:
                text = self.register_p.get_code_erro_element().text
        except:
            text = None     
        return text
        '''
        selenium 获取元素相关的信息（元素大小、元素内文本、元素可见&可用&选中&属性）
        size：元素的大小

        text：元素内文本

        is_displayed( )  ：元素是否可见

        is_enabled()： 元素是否可用（一般用于判断按钮是否置灰）

        is_selected( ) ： 元素是否被选中（一般用于表单中的单选框和复选框）

        get_attribute ( ) ： 元素的属性（可以获取到所选标签内的属性信息）
        '''
    
    #点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()
    
    #获取注册按钮文字
    def get_register_text(self):
        return self.register_p.get_button_element().text