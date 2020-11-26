#coding = utf-8
'''
unittest框架基础用法
'''
import unittest #unittest类库是selenium自带的，可直接引用
class FirstCase01(unittest.TestCase):    #新建的类想用unittest必须引用unittest.Test类库 
    
    @classmethod   #装饰器
    def setUpClass(cls):
        print('这是所有case执行之前的前置')
        
    @classmethod #装饰器
    def tearDownClass(cls):                         #tearDownClass()和setUpClass使用时，要有装饰器
        print('这是所有case执行之后的后置')
        
    def setUp(self):
        print('这个是每条case的前置条件')
        
    def tearDown(self):
        print('这个是每个case的后置条件')
        
    def testfirstcase01(self):           #引用unittest类库，建立的测试用例必须以test开头
        print('这是第一条case')
    
    def testfirstcase02(self):
        print('这是第二条case')
        
if __name__ == "__main__":               #引用unittest，当前文件运行时，就不需要再写个main函数，不需要再将类实例化
    unittest.main()                      #测试用例的执行顺序是根据字母或数字升序执行的
    
