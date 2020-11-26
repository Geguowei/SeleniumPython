#  获取静态方法和类方法
'''
反射getattr学习，详细件文档
'''
class Teacher(object):
    #类的静态属性
    dict = {'查看学生的信息':'show_student','查看讲师的信息':'show_teacher'}
 
    def __init__(self,name,age):
        self.name = name
        self.age = age
 
    #类方法
    @classmethod
    def func(cls):
        print('类方法')
 
    #静态方法
    @staticmethod
    def func1():
        print('静态方法')
 
    def show_student(self):
        print('show_student...')
 
    def show_teacher(self):
        print('show_teacher...')
#   反射类方法和静态属性
# getattr（）方法
#第一个参数是对象(一切皆对象,类也是对象),第二个参数是属性的字符串形式
attr = getattr(Teacher,'dict')
print(attr)         #{'查看学生的信息': 'show_student', '查看讲师的信息': 'show_teacher'}
func = getattr(Teacher,'func')
func()       #类方法
 
#2获取对象的属性值和普通方法
#获取属性
teacher = Teacher('zs','123')
name = getattr(teacher,'name')
print(name)  #zs
#获取方法
show_student = getattr(teacher,'show_student')
show_student()   #show_student...