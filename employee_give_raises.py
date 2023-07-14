#题目：雇员 编写一个名为Employee 的类，其方法__init__()接受名和姓和年薪，并将他们存储在属性中。编写一个名为give_raise()的方法，它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。

class Employee:
    '''创建雇员信息'''

    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        #设置默认年薪为5000元
        self.salary=5000

        
        
        

    def give_raise(self,salary):
        
        #若没有指定更要增加的年薪，则使用默认年薪
        if salary == 0:
            self.salary = 5000
        else:
            self.salary += salary
        #print(f"年薪：{self.salary}")
    

    

my_employee=Employee("思玉",'郑')
my_employee.give_raise(1000)
print(f'姓名：{my_employee.last_name}{my_employee.first_name},年薪：{my_employee.salary}')

