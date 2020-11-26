#coding = utf-8
'''
unittest框架，@unittest.skipif使用
1.1 @unittest.skip(reason)
reason是跳转的原因，强制跳过

1.2 @unittest.skipIf(condition，reason)
有条件的跳转，如果condition为真，则跳过

1.3 @unittest.skipUnless(condition，reason)
有条件的跳转，如果condition为假，则跳过

1.4 @unittest.expectedFailure
如果test失败了，这个test不计入失败的case数目
'''
import unittest


class FirstCase05(unittest.TestCase):
    globals()['status'] = 200  

    @classmethod
    def setUpClass(cls):
        cls.url = "http://www.baidu.com"

    def test_1_alien(self):
        print("test_1_status：", globals()['status'], id(globals()['status']))

    def test_2_alien(self):
        globals()['status'] = 404
        print("test_2_status", globals()["status"], id(globals()['status']))

    @unittest.skipIf(globals()['status'] == 200, "status为200，跳过测试用例")
    def test_3_alien(self):
        print("test_3_status:", globals()['status'])

    def test_4_alien(self):
        print("test_4_status", globals()["status"], id(globals()['status']))


if __name__ == '__main__':
    unittest.main()