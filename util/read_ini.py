#coding=utf-8
import configparser
class ReadIni(object):
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = "D:/selenium_lianxi_demo/config/LocalElement.ini"#配置文件路径
        if node == None:
            self.node = "RegisterElement" #配置文件的【】分组,即section
        else:
            self.node = node
        self.cf = self.load_ini(file_name) #调用该包（util.read_ini）ReadIni类下面的load_ini方法直接运行
    #加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser() #引用configparser模块读写配置文件
        cf.read(file_name) #读文件内容
        return cf
    '''
    脚本解析
    cf.read(filename)：读取文件内容

    cf.sections()：得到所有的section，并且以列表形式返回

    cf.options(section)：得到section下所有的option

    cf.items(option)：得到该section所有的键值对

    cf.get(section,option)：得到section中option的值，返回string类型的结果

    cf.getint(section,option)：得到section中option的值，返回int类型的结果
    
    cf.write(filename)：将configparser对象写入.ini类型的文件

    cf.add_section()：添加一个新的section

    cf.add_set(section,option,value)：对section中的option信息进行写入
    
    cf.read(filename)：读取文件（这里需要注意的是：一定要先读取文件，再进行修改）

    cf.remove_section(section)：删除文件中的某个section的数值

    cf.remove_option(section,option)：删除文件中某个section下的option的数值
    '''
    #获取value得值
    def get_value(self,key):
        data = self.cf.get(self.node,key) #得到section(self.node)中option(key)的值，返回string类型的结果
        return data
    

# if __name__ == '__main__':
#     read_init = ReadIni()
#     print(read_init.get_value('user_name'))

