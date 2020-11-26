#coding = utf-8
'''
如何大量运行case文件
运行所有的case文件
'''
import unittest
import os

class RunCase(unittest.TestCase):
    def test_running(self):
        case_path = os.getcwd()
        runner_path = os.path.join(case_path,'case')
        suit = unittest.defaultTestLoader.discover(runner_path,'unittest_case*.py',top_level_dir=None)
        unittest.TextTestRunner().run(suit)
        
if __name__ == "__main__":
    unittest.main()