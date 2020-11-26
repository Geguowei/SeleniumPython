#coding=utf-8
from handle.register_handle import RegisterHandle
class RegisterBusiness(object):
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)
    
    def user_base(self,email,name,password,code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()
        self.register_h.get_register_text()
    
    def register_success(self):
        if self.register_h.get_register_text() ==None:
            return True
        else:
            False
            
    #实现ddt数据驱动
    def register_function(self,email,username,password,code,assertCode,assertText):
        self.user_base(email,username,password,code)
        if self.register_h.get_user_text(assertCode,assertText) ==None:
            return True
        else:
            return False

        
    
    #email错误
    def login_email_erro(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('user_email_erro',"请输入有效的电子邮件地址")==None:
            print("邮箱检验成功")
            return True
        else:
            print('输入的邮箱名有误')
            return False
        
        
    #name错误
    def login_name_erro(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('user_name_erro',"字符长度必须小于等于18，一个中文字算2个字符")==None:
            return True
        else:
            print("用户名检验不成功")
            return False
        
    #password错误
    def login_password_erro(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('password_erro',"最少需要输入 5 个字符")==None:
            return True
        else:
            print("密码检验不成功")
            return False
        
    #code错误
    def login_code_erro(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('code_text_erro',"验证码错误")==None:
            print("验证码不成功")
            return True
        else:
            return False
