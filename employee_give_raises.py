

class Employee:
    '''创建雇员信息'''

    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=0
        print(f'姓名：{last_name}{first_name},年薪：{self.give_raise(self.salary)}')
        
        

    def give_raise(self,salary):
        
        if salary != 0:
            self.salary+=salary
        else:
            self.salary += 5000
        print(f"年薪：{self.salary}")
    

    

my_employee=Employee("思玉",'郑')
my_employee.give_raise(0)





