#coding=utf-8
import sys
sys.path.append(r'D:\selenium_lianxi_demo')#添加当前工程目录
from keywordselenium.actionMethod import ActionMethod
from util.excel_util import ExcelUtil

'''
关键字测试用例
关键字模型，思维很重要，根据关键字对测试用例进行操作
'''
class KeywordCase:
    def run_main(self):
        #实类化，并且为公用
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil('D:\selenium_lianxi_demo\config\keyword.xls')
        #拿到行数
        #循环行数，去执行每一行的case
        #if 是否执行
            #拿到执行方法
            #拿到操作值
            #拿到输入数据
            #if 是否有输入数据
                #执行方法（输入数据，操作元素）
            #if 没有输入数据
                #执行方法（操作元素）
        case_lines = handle_excel.get_lines()               #拿到excel的总行数
        if case_lines:
            for i in range(1, case_lines):
                #第4列，列属性为是否执行，遍历所有行，即遍历所有测试用例 
                is_run = handle_excel.get_col_value(i,3)
                #执行为yes的测试用例
                if is_run == 'yes':
                    #执行方法，找到i行，执行方法列的单元格值；即反射的ActionMethod类方法
                    method = handle_excel.get_col_value(i,4)
                    
                    #输入数据，找到i行，输入数据列的单元格值；反射的ActionMethod类方法的参数值                   
                    send_value = handle_excel.get_col_value(i,5)
                    
                    #操作元素，找到i行，操作元素列的单元格值；反射的ActionMethod类方法的参数值                   
                    handle_value = handle_excel.get_col_value(i,6)
                    
                    #预期结果（方法），找到i行，预期结果（方法）列的单元格值；即反射的ActionMethod类方法 ;该方法为预期结果的断言方法判断               
                    except_result_method = handle_excel.get_col_value(i,7)
                    
                    #实际结果，找到i行，实际结果列的单元格值；实际结果即预期对比结果，判断True or False               
                    except_result = handle_excel.get_col_value(i,8)
                    #''而不是None
                    #if send_value:
                    
                    #handle,操作，映射，执行
                    self.run_method(method,send_value,handle_value)
                    
                    #下面一大串是先根据实际结果即预期结果，决定怎么执行映射后的方法，要不要传递参数（此处参数为实际结果list[1]的值），然后执行，最后根据执行结果进行判断
                    #判断有无实际结果即预期结果，有
                    if except_result != '':
                        #将实际结果即预期对比结果送到def get_except_result_value进行切片，返回list
                        except_value = self.get_except_result_value(except_result)
                        #如果list【0】等于text，即根据文本判断测试用例通过与否
                        if except_value[0] =='text':
                            #执行映射后ActionMethod()类中的except_result_method方法，即预期结果判断方法
                            result = self.run_method(except_result_method)
                            #实际结果即预期对比结果，与ActionMethod()类中的except_result_method方法，即预期结果判断方法返回数据比较；实际结果文本在执行返回的数据中，测试通过
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        #如果list【0】等于element,即根据元素判断测试用例通过与否
                        elif except_value[0] == 'element':
                            '''
                            将实际结果即预期对比结果的元素信息（此处的元素信息是localElement.py的section节点），放到映射后ActionMethod()类中的except_result_method方法中执行，返回对应方法返回值;
                            找到了对应元素与实际结果一致，测试用例通过
                            '''
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        else:
                            print('没有else')
                    else:
                        print('实际结果即预期结果值为空')
                                
                                
    #获取预期结果
    def get_except_result_value(self,data):
        return data.split('=')                      #对data，类型为list，进行切片
    
    #handle、映射
    def run_method(self,method,send_value='',handle_value=''):
        #ActionMethod()映射，第一个函数实类化过了，并且是全局的，直接拿过来映射；@method，查找映射后ActionMethod()类中的方法或属性，直接用
        method_value = getattr(self.action_method,method)
        
        #此处的判断用于映射ActionMethod()类中的方法后，需不需要传参数，以及传几个，映射的语法做出对应的输入使用
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        elif send_value == '' and handle_value == '':                     #因为是判断excel的数据，所以没有none，要么空，要么有值，None在这也算一种值
            result = method_value()  
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value(send_value,handle_value)
        return result     #参数化，return后与def run_main中的result变量进行比较判断          
            
            
if __name__ == '__main__':
    test = KeywordCase()
    test.run_main()
                  
