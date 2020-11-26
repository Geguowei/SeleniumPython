#coding = utf-8
import logging
import os
import datetime

class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        #定义longger的级别未debug，设置等级
        self.logger.setLevel(logging.DEBUG)

        #控制台输出日志，StreamHandler流可以将结果输出在控制台，自己调试是用的，不加，控制台看不到结果，目前这个脚本，最下方的debug会在控制台和日志文件同时输出，不加这两行代码，控制台就没有结果
        consle = logging.StreamHandler()
        self.logger.addHandler(consle)

        #文件名字
            #base_dir使用绝对路劲，是因为该脚本和日志路径不一样，日志的路径还在脚本的再一个文件夹目录里面
        base_dir = os.path.dirname(os.path.abspath(__file__))   #os.path.abspath(__file__)返回当前文件的绝对路径，包含文件名；os.path.dirname（文件路劲\文件名.py）去掉文件名，返回路径
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name = log_dir+"/"+log_file
        print(log_name)
        #文件输出日志,FileHandler文件形式的一个输出流
        # file_handle = logging.FileHandler('D:\\selenium_lianxi_demo\\log\\logs\\test.log')
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')  #'a',encoding='utf-8'不是必要的，加了encoding='utf-8'在VScode中可以查看中文
        self.file_handle.setLevel(logging.INFO) #INFO级的debug才打印到日子
        formatter = logging.Formatter('%(asctime)s %(filename)s- at %(lineno)d line  ---> %(funcName)s %(levelno)s:%(levelname)s ---> %(message)s') #日志格式定义，可以进到Formatter里面查看具体哪些
        self.file_handle.setFormatter(formatter)  #将日志格式放到对应流中
        self.logger.addHandler(self.file_handle)

        # self.logger.debug("今晚加个班")
        self.logger.info("今晚加个班")


        
    def get_log(self):
        return self.logger

        
    def close_handle(self):
        self.file_handle.close()       #关闭流
        self.logger.removeHandler(self.file_handle)
     
    '''
    log以装饰器功能实现尚未掌握
    def log(func):
        def wrapper(*args, **kwargs):
            print("现在开始执行函数：",func.__name__)
            func()
            return wrapper



    @log 
    def test_login(self):
        print("函数的执行")
    '''

        
if __name__ == "__main__":
    user = UserLog()
    log = user.get_log()
    logger = log.info('搞起来')
    user.close_handle()
