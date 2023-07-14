import unittest
from employee_give_raises import Employee

#题目：为Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_raise() 和 test_give_custom_raise()。使用方法 setUp()，以免
#      在每个测试用例方法中都新建雇员实例。运行这个测试用例，确认两个测试用例都通过了。

class TestEmployeeraises(unittest.TestCase):
    '''针对雇员信息类的测试'''

    def setUp(self):

        '''创建一个雇员和年薪的两种情况'''
       
        self.my_employee=Employee("思玉",'郑')
        self.salary=[0,1000]
        self.salaries=[5000,6000]
        
    def test_give_default_raise(self):

        '''测试使用默认年薪，取salary为0的情况进行测试'''

        salaries=self.my_employee.give_raise(self.salary[0])

        '''判断默认年薪是否与预期一致'''
        self.assertEqual(salaries,5000)

    def test_give_custom_raise(self):
        '''测试两种年薪情况，遍历两种年薪情况'''
        for salary in self.salary:

            '''分别取出两种年薪情况的值'''
            salaries=self.my_employee.give_raise(salary)

            '''判断两种年薪情况的值是否在预期的值中'''
            self.assertIn(salaries,self.salaries)



if __name__ == '__main__':
    unittest.main()