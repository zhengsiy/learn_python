#144
class Restaurant:
    '''一次模拟餐馆的简单尝试'''
    def __init__(self,name,type):
        '''初始化餐馆名字和类型属性'''
        self.name=name
        self.type=type
        self.number_served=0
    
    
    def describe_restaurant(self):
        '''简单描述餐馆情况'''
        print(f'{self.name} is a {self.type}') 
    
    def open_restaurant(self):
        '''餐馆营业情况'''
        print(f'{self.name} is openning! welcome to {self.name}')


    def read_number_served(self,eat_num):
        '''设置餐馆就餐人数'''
        self.number_served=eat_num
        print(f'\n就餐人数为{self.number_served}')



    def increment_number_served(self,increment_num):
        self.number_served=+increment_num
        print(f'\n这桌客人加了{increment_num}个人现在这桌客人总共有{self.number_served}个人')


my_restaurant=Restaurant('好滋味','Chinese restaurant')
your_restaurant=Restaurant('真好吃','Western restaurant')
her_restaurant=Restaurant('极好恰','italian meal')

print(f"\nmy restaurant's name is {my_restaurant.name}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(f"\nyour restaurant's name is {your_restaurant.name}")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

print(f"\nher restaurant's name is {her_restaurant.name}")
her_restaurant.describe_restaurant()
her_restaurant.open_restaurant()


#149
restaurant=Restaurant('好滋味','Chinese restaurant')
restaurant.number_served=2
print(f'今天{restaurant.name}餐馆接待了{restaurant.number_served}个人')

restaurant.read_number_served(6)

restaurant.increment_number_served(2)






class User:
    '''一次模拟用户的简单尝试'''
    def __init__(self,first_name,last_name,age,sex,login_attempts) -> None:
        self.firstname=first_name
        self.lastname=last_name
        self.age=age
        self.sex=sex
        self.login_attempts=0

    def describe_user(self):
        '''简要描述用户信息'''
        print(f"\n{self.lastname}{self.firstname} is a {self.sex}.")
    
    def greet_user(self):
        print(f"Hello,{self.lastname}{self.firstname}!")


    def increment_login_attempts(self):
        self.login_attempts+=1
        print(self.login_attempts)


    def reset_attempts(self):
        self.login_attempts=0
        print(self.login_attempts)

    


user1=User('siyu','zheng','23','girl',0)
print(f"\n{user1.lastname.title()}{user1.firstname} is {user1.age} years old {user1.sex}!")

user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_attempts()


user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_attempts()





#P155
class IceCreamStand(Restaurant):
    '''继承之前的 Restaurant 类'''

    #初始化父属性
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors=['vanilla','chocolate','milk']

    def describe_flavors(self):
        print(f'we have ice cream in these flavors:{self.flavors}')

my_flavors=IceCreamStand('meyijia','ice cream shop')
my_flavors.describe_restaurant()
my_flavors.describe_flavors()
      

class Privileges:
    '''管理员特权管理'''

    def __init__(self) -> None:
        self.privileges=['can add post','can delete post','can ban user']

    def show_privileges(self):
        print(f'管理员拥有以下几个权限：{self.privileges}')

class Admin(User):
    '''管理员的特殊权限'''

    def __init__(self, first_name, last_name, age, sex, login_attempts) -> None:
        super().__init__(first_name, last_name, age, sex, login_attempts)
        self.privileges=Privileges()

    def describe_user(self):
        print(f"\n{self.lastname}{self.firstname} is a admin.")

    def des_privileges(self):
        print(f'{self.lastname}{self.firstname} have {self.privileges} privileges')
    


xinwang=Admin('xin','wang',26,'boy',1)

xinwang.privileges.show_privileges()



        
    


