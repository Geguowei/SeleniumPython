'''
BeautifulReport.py测试报告，未搞成功
'''
#coding=utf-8
from BeautifulReport import BeautifulReport
import unittest
from second_case import Second
import os
import time

current_path = os.getcwd()
report_path = os.path.join(current_path, "Report")
now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

# 报告地址&名称
report_title = 'Example报告' + now + ".html"     # 如果不能打开这个文件，可能是now的格式，不支持：和空格

# 报告描述
desc = '用于展示修改样式后的HTMLTestRunner'

if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.makeSuite(Second))
    run = BeautifulReport(testsuite)
    run.report(description=desc, filename=report_title, log_path=report_path)