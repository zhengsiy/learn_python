#最简单的函数
#先定义一个名为greet_users的函数，greet_users即为函数名
def greet_users():    #圆括号内可指出函数为完成什么样的任务需要什么样的信息，为空即不需要任何信息也能完成下面的任务
    '''显示简单的问候语'''     #所有函数名后缩进的内容构成函数体，即函数需要完成的任务封装在里面
    print('Hello!')      #该函数现在的任务就是完成打印“Hello”的任务
greet_users()            #调用该函数,圆括号中可填入函数为完成任务所需要的信息


#给函数传参
def greet_users(username):     #要求在执行函数时给这个函数传入一个值，即函数完成工作时所需要的信息，这个为形参
    print(f'Hello!{username}')
greet_users('zhengsiyu'.title())  #‘zhengsiyu’即传给函数的值，即传递给函数的信息，这个为实参


#位置实参,形参和实参的位置顺序一一对应
def pets_message(animal_type,pet_name):
    '''显示宠物的信息'''
    print(f'\nI have a {animal_type}!')
    print(f"My {animal_type}'s name is {pet_name}")
pets_message('Hamster','Harry')
pets_message('Dog','Kuqi')

#关键字实参:不用考虑实参所对应的位置，
pets_message(animal_type='Cat',pet_name='Candy')
pets_message(pet_name='candy',animal_type='Cat')

#设置默认值
# 需要将设置了默认值的那个形参放在最后，因为已经设置了一个形参的值，所以在调用函数时只需要传入一个实参即可，
# python依然将这个实参视为位置实参，所以需要将设置了默认值的那个形参放在最后
def pets_message(pet_name,animal_type='Dog'):
    '''显示宠物的信息'''
    print(f'\nI have a {animal_type}!')
    print(f"My {animal_type}'s name is {pet_name}")

pets_message('willie')    #调用时只传入pet_name的值即可
pets_message(pet_name='Cindy',animal_type='Bird')     #若重新给设置了默认值的形参传一个新的值，那么将忽略默认值，而使用这个新值



def get_formatted_name(first_name,last_name):
    full_name=f'{first_name}{last_name}'
    return full_name.title()
musician=get_formatted_name('zheng','siyu')
print(musician)

def get_formatted_name(first_name,last_name,middle_name=''):
    '''返回整洁的姓名'''
    if middle_name:
        full_name=f'\n{first_name}{middle_name}{last_name}'
    else:
        full_name=f'\n{first_name}{last_name}'
    return full_name.title()
musician=get_formatted_name('zheng','siyu')
print(musician)
musician=get_formatted_name('zheng','siyu','hui')
print(musician)


def build_person(first_name,last_name,age=None):
    '''返回一个字典，其中包含有关一个人的信息'''
    if age:
        person={'first':first_name,'last':last_name,'age':age}
    else:
        person={'first':first_name,'last':last_name}
    return person
musician=build_person('xin','wang',23)
print(musician)


def build_person(first_name,last_name,age=None):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_person('xin','wang',25)
print(musician)





def get_formatted_name(first_name,last_name):
    full_name=f'{first_name}{last_name}'
    return full_name
while True:
    print('\n请告诉我你的名字，按“q”可退出程序')
    f_name=input('\n请输入你的姓：')
    if f_name=='q':
        break
    else:
        l_name=input('请输入你的名字：')
        if l_name=='q':
            break
       
        formatted_name=get_formatted_name(f_name,l_name)
        print(formatted_name)



#给函数中传递列表
user_names=['zhengsiyu','xinwang','huanhuan']
def greet_users(names):
    for name in names:
        print(f'\nHello,{name}')
greet_users(user_names)


#在函数中修改列表

unprited_designs=['phone case','robot pendant','dodecahedron']
completed_models=[]
def print_models(unprinted_designs,completed_models):
    '''模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到已完成的列表中'''
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f'\n正在打印{current_design}')
        completed_models.append(current_design)
print_models(unprited_designs,completed_models)

def show_completed_models(completed_models):
    '''显示打印好的所有模型'''
    print(f'\n这些是已经打印好的模型：')
    for completed_model in completed_models:
        print(completed_model)
show_completed_models(completed_models)



#要保留原列表的数据，可使用原列表的副本
#    funtion_name(list_name[:])：调用函数时在需要传入的那个列表做切片，即复制一个副本
#例如：调用print_models函数，传入unprited_designs列表，加[:]做切片创建unprited_designs的副本
print_models(unprited_designs[:],completed_models)



#传递任意数量的实参
def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    print(f'\n这是您选的配料，请确认：{toppings}')
make_pizza('mushrooms','extra chess')


