#coding = utf-8
'''
数据驱动ddt的使用
'''
import ddt
import unittest

@ddt.ddt #装饰测试类 
class DataTest(unittest.TestCase):
    def setup(self):
        print('这个是setup')
    
    def tearDown(self):
        print('这个是teardown')
        
    @ddt.data(
        [1,2],
        [3,4],
        [5,6]
    )#装饰测试方法,装载数据，声明数据
    
    @ddt.unpack  #用来拆解数据
    def test_add(self,a,b):
        print(a+b)
        
if __name__ == "__main__":
    unittest.main()
    
    
    
