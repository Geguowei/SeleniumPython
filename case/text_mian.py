#coding = utf-8
'''
服务main文件夹unittest.defaultTestLoader()
'''
import unittest 
class text_main_text(unittest.TestCase):    
    
    @classmethod   #装饰器
    def setUpClass(cls):
        print('这是所有unittest.defaultTestLoader()的case执行之前的前置')
        
    @classmethod #装饰器
    def tearDownClass(cls):                         
        print('这是所有case执行之后的后置')
        
    def setUp(self):
        print('这个是每条case的前置条件')
        
    def tearDown(self):
        print('这个是每个case的后置条件')
        
    @unittest.skip('不执行第一条case')   
    def testfirstcase01(self):           
        print('这是第一条case')
        
    @unittest.skip('不执行第二条case')
    def testfirstcase02(self):
        print('这是第二条case')
        
    def testfirstcase03(self):
        print('这是第三条case')
        
if __name__ == "__main__":               
    suit = unittest.TestSuite()     #新增变量定义为unittest容器
    suit.addTest(text_main_text('testfirstcase02')) #unittest.TestSuite.addTest(测试用例类（'具体增加的测试用例'）)
    suit.addTest(text_main_text('testfirstcase03'))
    suit.addTest(text_main_text('testfirstcase01'))
    unittest.TextTestRunner().run(suit)          #unittest.TextTestRunner().run()执行容器中的测试用例，容器中测试用例的执行顺序是添加的先后顺序决定的
