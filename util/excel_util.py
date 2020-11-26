#coding = utf-8
'''
excel操作
xlrd读取xls文件内容,使用前需要先进行安装，pip install xlrd
xlutils写xls文件，pip install xlutils
xlwt也可以写，xlutils有的功能，xlwt没有，比如拷贝sheet，最加多行数据，修改xls函数等，pip install xlwt
'''
import xlrd                          #导入xlrd
from xlutils.copy import copy
class ExcelUtil:
    def __init__(self,excel_path=None,index=None):           #不是必要参数，赋值None
        if excel_path ==None:
            self.excel_path = "D:\selenium_lianxi_demo\config\casedata.xls"
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)     #打开xls文件
        self.table = self.data.sheets()[index]         #xls文件的sheet页,不传默认为0，即第一页
        
    #获取excel行数
    def get_lines(self):
        rows = self.table.nrows                   #获取sheet的总行数
        # self.rows = self.table.ncols                   #获取sheet的总列数
        if rows >= 1:
            return rows
        else:
            return None
        
        #获取excel列数
    def get_cols(self):
        cols = self.table.ncols                   #获取sheet的总列数
        if cols >= 1:
            return cols
        else:
            return None
    
    #获取单元格的数据
    def get_col_value(self,row,col):
        if self.get_lines() > row :
            data = self.table.cell(row,col).value
            return data
        else:
            return None
        
    #获取所有行或列的数据
    def get_data(self):
        #获取的数据以两个list嵌套，即【【】，【】】
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(self.get_lines()):                 # 循环sheet的行数
                col = self.table.row_values(i)         #以list形式，获取i行的数据
                # col = self.table.col_values(i)          ##以list形式，获取i列的数据
                result.append(col)                     #添加到list，result中
            return result
        else:
            return None
    '''
    for i in range ()作用：

        range()是一个函数， for i in range () 就是给i赋值：

        比如 for i in range （1，3）：

        就是把1,2依次赋值给i

        range () 函数的使用是这样的:

        range(start, stop[, step])，分别是起始、终止和步长

        range（3）即：从0到3，不包含3，即0,1,2
    '''
    #根据已知行和单元格值，求列坐标,不传行数，默认为第一行
    def location_col(self,col_val,row=None):
        cols = self.table.ncols                               #拿到sheet总共有多少列
        if row != None:
            name=self.table.row_values(row)                   #找到这一行所有数据
        else:
            name=self.table.row_values(0)
        for i in range(cols):                                 #i遍历cols总列数    
            if name[i]==col_val:                              #i放到刚刚取的一行数据["","",""]中查找对应值,行数据是列表形式存在的
                val = i
                return val 
                  
    #copy并写入数据,目前写入就是keyword。xls【实际结果】这一列数据,
    def write_value(self,row,value):
        read_value = xlrd.open_workbook(self.excel_path)                 #打开放在写write这边，可以保证写的都是延续最新的
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,9,value)                       #ecxel,report在第10列，即9
        write_data.save(self.excel_path)        
        
if __name__ == "__main__":
    ex = ExcelUtil("D:\selenium_lianxi_demo\config\keyword.xls")                    #实例化ExcelUtil类
    # print(ex.get_data())
    # print (ex.get_col_value(2,2))
    print (ex.write_value(3,7,"预期结果aaa"))
    