#coding = utf-8
'''
unittest.defaultTestLoader(): defaultTestLoader()类，通过该类下面的discover()方法可自动更具测试目录start_dir匹配查找测试用例文件（test*.py），并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover。用法如下：

discover=unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
'''
import os
import unittest

cash_path=os.path.join(os.getcwd(),'case')      #os.getcwd() 获得目录的当前系统程序工作路径；os.path.join（）拼接出多级目录
print(os.getcwd())                 
print(cash_path)
discover = unittest.defaultTestLoader.discover(cash_path,pattern="text*.py",top_level_dir=None)  #unittest.defaultTestLoader.discover（路径，pattern=‘匹配模糊文件名’，top_level_dir=None）

if __name__ == "__main__":
    runner=unittest.TextTestRunner()
    runner.run(discover)