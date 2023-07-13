from random import randint,choice,sample

#先创建一个Dog类
class Dog:
    '''一次模拟小狗的简单尝试'''
    def __init__(self,name,age):   #_init_函数是特殊函数，每次根据Dog类创建新实例时python都会自动运行它。即根据Dog类创建的每个实例都将储存名字和年龄
        '''初始化属性name和age'''
        self.name=name
        self.age=age

    def sit(self):
        '''模拟小狗收到命令时蹲下'''
        print(f'{self.name} is now sitting.')
    
    def roll_over(self):
        '''模拟小狗收到命令时打滚'''
        print(f'{self.name} is now roll_over.')


my_dog=Dog('candy','5')
your_dog=Dog('lucky','6')
print(f'{my_dog.name} is {my_dog.age} years old.')

#调用方法。根据Dog类创建实例后，就能使用句点表示法来调用Dog类中定义的任何方法了
my_dog.sit()
my_dog.roll_over()

print(f'\n{your_dog.name} is {your_dog.age} years old.')
your_dog.sit()
your_dog.roll_over()



class Car:
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year) -> None:
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0   #给属性指定默认值

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name=f'{self.year} {self.make} {self.model}'
        return long_name
    
    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print(f'\nThis car has {self.odometer_reading} mileson it!')

    def update_odometer(self,milege):   #更新里程这一属性的值，添加了一个形参milage，调用该方法时传入形参的值即可
        '''将里程表读数设置为指定值,且禁止任何人将里程表的读数往回调'''
        if milege>=self.odometer_reading:
            self.odometer_reading=milege
        else:
            print("you can't roll back an odometer!")

    def increment_odomenter(self,miles):
        '''将里程表读数增加至指定的量'''
        self.odometer_reading+=miles



my_car=Car('audi','A4','2019')
print(my_car.get_descriptive_name())
my_car.read_odometer()     #调用实例 my_car 中的 read_odometer信息

my_car.odometer_reading=23   #直接通过实例修改属性的值
my_car.read_odometer()

my_car.update_odometer(45)   #将45传给形参milage
my_car.read_odometer()

my_car.update_odometer(5)
my_car.read_odometer()



your_car=Car('benze','C260','2019')
print(your_car.get_descriptive_name())

your_car.update_odometer(780)
your_car.read_odometer()

your_car.increment_odomenter(80)
your_car.read_odometer()


#将实例用作属性
class Bettery:
    def __init__(self,bettery_size=70):
        self.bettery_size=bettery_size

    def describe_battery(self):
        '''打印一条显示电瓶容量的信息'''
        print(f'my car has a {self.bettery_size}-kwh battery!')

    def upgrade_battery(self):
        '''检查电瓶容量'''
        if self.bettery_size!=100:
            self.bettery_size==100
            print(f'my car has a {self.bettery_size}-kwh battery!')

my_tesla=Bettery()
my_tesla.upgrade_battery()

#继承
class ElectricCar(Car):
    '''电动汽车的独特之处'''
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        self.bettery_size=Bettery()   #给子类定义特有属性

    def describe_battery(self):   #给子类定义特有方法
        '''打印一条显示电瓶容量的信息'''
        print(f'{my_tesla.get_descriptive_name()} has a {self.bettery_size}-kwh battery!')

    
#my_tesla=ElectricCar('tesla','modle s',2019)
#print(my_tesla.get_descriptive_name())
#my_tesla.bettery_size.describe_battery()
#my_tesla.bettery_size.describe_battery()


class die:
    '''创建一个骰子来生成随机数'''
    def __init__(self) -> None:
        self.side=6

    def roll_die(self):
        print(randint(1,10))
        
my_die=die()
my_die.roll_die()


#彩票
lottery=['5','d','0','8','g','e','3','r','n','2','4','7','1','6','9']
print(sample(lottery,4))
print('if your lottery are the four digits which were printed,than you hit the jackpot!')

