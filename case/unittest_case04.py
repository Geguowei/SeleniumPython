#coding = utf-8
'''
unittest框架，用例执行case跳过
'''
import unittest 
class FirstCase04(unittest.TestCase):    
    
    @classmethod   #装饰器
    def setUpClass(cls):
        print('这是所有case执行之前的前置')
        
    @classmethod #装饰器
    def tearDownClass(cls):                         
        print('这是所有case执行之后的后置')
        
    def setUp(self):
        print('这个是每条case的前置条件')
        
    def tearDown(self):
        print('这个是每个case的后置条件')
     
    @unittest.skip('不执行第一条case')         #@unittest.skip(),测试用例跳过，（）中的内容为描述，控制套不输出，无影响  ，跳过可以跟条件判断结合使用   
    def testfirstcase01(self):           
        print('这是第一条case')
        
    @unittest.skip('不执行第二条case')    
    def testfirstcase02(self):
        print('这是第二条case')
        
    def testfirstcase03(self):
        print('这是第三条case')
        
if __name__ == "__main__":               
    suit = unittest.TestSuite()     
    suit.addTest(FirstCase04('testfirstcase02')) 
    suit.addTest(FirstCase04('testfirstcase03'))
    suit.addTest(FirstCase04('testfirstcase01'))
    unittest.TextTestRunner().run(suit)          #不管是容器中已经添加的测试用例或者unittest.main()全部执行，只要测试用例有@unittest.skip()，那么这条测试用例都会跳过
    
