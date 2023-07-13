# P36页
'''
names=['zhengsiyu','lizhipeng','liuhongji']

print('由于郑思玉临时有事无法赴约，所以重新邀请了liujialong')
names[0]='liujialong'

print('找到了更大的餐桌，所以我将邀请更多的人共进晚餐')
names.append('yeweizhi')
names.insert(0,'songchao')
names.insert(2,'siyu')
print(names)
message=f'亲爱的{names[0].title()}，今天晚上七点想邀请你在海洋餐厅共进晚餐，期待你的光临!\n亲爱的{names[1].title()}，今天晚上七点想邀请你在海洋餐厅共进晚餐，期待你的光临!'
print(message)


print('由于新购买的餐桌无法送达，所以只能邀请两位嘉宾')
rem_p1=names.pop(0)
print(f'很抱歉由于特殊原因今晚无法邀请{rem_p1.title()}共进晚餐')
rem_p2=names.pop()
print(f'很抱歉由于特殊原因今晚无法邀请{rem_p2.title()}共进晚餐')
rem_p3=names.pop(0)
print(f'很抱歉由于特殊原因今晚无法邀请{rem_p3.title()}共进晚餐')
rem_p4=names.pop(1)
print(f'很抱歉由于特殊原因今晚无法邀请{rem_p4.title()}共进晚餐')


print(names)

n_message1=f'{names[0].title()}仍在共进晚餐名单之列，请准时参加！'
n_message2=f'{names[1].title()}仍在共进晚餐名单之列，请准时参加！'
print(n_message1,n_message2)

del names[1]
del names[0]
print(names)
'''

# P39页
fovrate_area=['xi an','si chuang','chong qin','yun nan','bei jing']
print(f'这是原始列表:{fovrate_area}')

print(f'这是不永久排序的列表：{sorted(fovrate_area)}')

print(f'这是原始列表:{fovrate_area}')

print(f'这是不永久排序且顺序相反的列表：{sorted(fovrate_area,reverse=True)}')

print(f'这是原始列表:{fovrate_area}')

fovrate_area.reverse()
print(fovrate_area)

fovrate_area.reverse()
print(fovrate_area)

fovrate_area.sort()
print(fovrate_area)

fovrate_area.sort(reverse=True)
print(fovrate_area)




#48
pizzas=['fruit_pizza','meat_pizza','vegetable_pizza']
for pizza in pizzas:
    print(pizza,end='.\n')
    print(f'I like {pizza}.\n')
print('I really like pizza!.\n' )


#49
annimals=['chicken','duck','goose']
for annimal in annimals:
    print(annimal)
    print(f'A {annimal.title()} would make a good pet.\n')
print('Any of these annimals would make good delicious!')


#50
cubes=[]
for cube in range(1,11):
    cube=cube**3
    cubes.append(cube)
print(cubes)
for cube in cubes:
    print(cube)

cubes=[cube**3 for cube in range(1,11)]
print(cubes)

#57
#num=cubes[0,3]
print(f'The first three items in the list are:{cubes[0:3]}')

print(f'Three items from the middle of the list are:{cubes[3:6]}')

print(f'Three items from the middle of the list are:{cubes[-3:]}')



my_foods=['方便面','面包','冰激凌']
friend_foods=my_foods[:]
my_foods.append('奶茶')
friend_foods.append('麻辣烫')
#打印结果方式一：
print(f'My favorite foods are:{my_foods}')
print(f'Friend favorites foods are:{friend_foods}\n')
#打印结果方式二：
print(f'My favorite foods are:')
print([m_foods for m_foods in my_foods])

print(f"\nfriend's favorate foods are:")
print([f_foods for f_foods in friend_foods])


foods=[]
for m_foods in my_foods:
    foods.append(m_foods)
print(foods)

#59
resturants=('鸡肉','羊肉','鱼肉','腊肉','鸭肉')
for resturant in resturants:
    print(resturant)
#resturants[1]='鹅肉'  元组无法修改里面的元素
#print(resturants)
resturants=('鸡肉','鹅肉','鱼肉','猪肉','鸭肉')
print(resturants)
for resturant in resturants:
    print(resturant)

#69

food=['VegaTable','Fruit']
print('Is car =="chiken",I predict false')
for fo in food:
    if fo=='chicken':
        print(False)
    else:
        print(True)
if 'vegatable' in food:
    print(f"真好，正合我口味")
if 'fruit' not in food:
    print('我再也不来了')
else:
    print('我下次还会再来的')
if food[0].lower()=='vegatable':
    print(True)
else:
    print(False)






a=3
b=9
if a<5:
    print(True)
else:
    print(False)
if a==3:
    print(True)
else:
    print(False)
if b>8:
    print(True)
else:
    print(False)
if a!=3:
    print(True)
else:
    print(False)
if a>=3 and b<=10:
    print(True)
else:
    print(False)
if a==4 or b==10:
    print(True)
else:
    print(False)

#75
alien_colors=['green','yellow','red']
if 'green' in alien_colors:
    print('该玩家获得了5分')
if 'orange' in alien_colors:
    print('该玩家可直接可晋级')
for alien_color in alien_colors:
    if alien_color=='green':
        print('该玩家因射杀外星人获得了5分')
    else:
        print('该玩家可获得10分')

if 'green' in alien_colors:
    print('\n该玩家可获得5分')
if 'yellow' in alien_colors:
    print('该玩家可获得10分')
if 'red' in alien_colors:
    print('该玩家可获得10分')


if alien_colors=='green':
    print('\n该玩家因射杀外星人获得了5分')
elif alien_colors=='yellow':
    print('该玩家可获得10分')
else:
    print('该玩家不可获得积分')


age=5
if age<2:
    print('这是个婴儿')
elif 2<=age<4:
    print('这是个幼儿')
elif 4<=age<13:
    print('这是个儿童')
elif 13<=age<20:
    print('这是个青少年')
elif 20<=age<65:
    print('这是个成年人')
else:
    print('这是个老年人')



#88
vocabulary={'function':'函数','module':'模块','default':'默认的'}
print(vocabulary['function'])
print(vocabulary['module'])
print(vocabulary['default'])
print(vocabulary.keys())

#94
for k,v in vocabulary.items():
    print(f'\nkeys:{k}')
    print(f'values:{v}')

vocabulary['space']='空格'
vocabulary['built_in']='内置的'
vocabulary['format']='格式'
vocabulary['digit']='数字'
print(vocabulary)


rivers={'nile':'egypt','amazom':'peru','yangtze':'china'}
for name,country in rivers.items():
    print(f'The {name.title()} runs through {country.title()}')
    print(name.title())
    print(country.title())

favorite_languages={'yewezhi':'java','liujialong':'c','zhengsiyu':'python','lizhipeng':'ruby','liuhongji':'php'}
investigators=['zhengsiyu','liuhongji','xinwang']
for investigator in investigators:
    if investigator in favorite_languages.keys():
        print(f'Hello,{investigator.title()},thank you to participate in our survey!')
    else:
        print(f'Hello,{investigator},welcome to participate in our survey!')




#100
people=[{'firstname':'zheng','last_name':'siyu','age':23,'location':'江西万载'},
        {'firstname':'liu','last_name':'hongji','age':21,'location':'广东韶关'},
        {'firstname':'li','last_name':'zhipeng','age':22,'location':'广东深圳'}]
for info in people:
    print(f'\n {info["firstname"]}{info["last_name"]} is {info["age"]} years old, and comes from {info["location"]}!')


favorite_places={'zhengsiyu':'云南大理','xinwang':'四川','zhongchunmei':'厦门'}
for name,place in favorite_places.items():
    print(f'\n {name.title()}：{place}')

number={'zhegnsiyu':[6,9,8],'liuhongji':[16,28,919,5.3],'liujialong':[2,17,11,19]}
for name,num in number.items():
    num=','.join(str(i)for i in num)
    print(f'\n{name.title()} favoraite number are {num} !')

#104
cars=['大众','丰田','本田','奔驰','宝马']
hired_car=input('please tell me whice kind of cars you want hire: ')
print(f'Let me see if i can find you a {hired_car}')
if hired_car in cars:
    print('I have find the car you want!')
else:
    print("sorry,we don't find the car you want!")


num=input('Please tell me how many people have dinner together?')
num=int(num)
if num >8:
    print(f'sorry,there are not table for {num} people!')
else:
    print(f'there is a table for {num} people')

num=input('enter you number:')
num=int(num)
if num % 10 ==0:
    print('这个数是10的整数倍')
else:
    print('这个数不是10的整数倍')


#110
list=[]
prompt='\nInput the ingredient you wanted:'
prompt+='\n(and enter "quit" when you finished !)'
activate=True
while activate:
    message=input(prompt)
    if message=='quit':
        activate=False
    else:
        list.append(message)
        print(f'\n\tYou have add {message} succesfully')

print(list)



prompt='请输入你的年龄：'
prompt+='按下‘quit’则退出程序'
activate=True
while activate:
    message=input(prompt)
    if message=='quit':
        break

    message=int(message)
    if message<3:
        print('你可以免费获得一张门票')
    elif message<=12:
        print('你的门票费用为$10')
    else:
        print('你的门票费用为$15')
    



#113
sandwich_orders=['sahla sandwich','vegetable sandwich','bacon sandwich']
finished_sandwich=[]
while sandwich_orders:
    sandwich_order=sandwich_orders.pop()
    print(f'\nI made your {sandwich_order}!')
    finished_sandwich.append(sandwich_order)

print(f'\nthere are all finished sandwich:{",".join(str(i)for i in finished_sandwich)}')


sandwich_orders=['sahla sandwich','vegetable sandwich','sahla sandwich','bacon sandwich','sahla sandwich']
print(f'\nsahla sandwich have been sold!')
activate=True
while activate:
    if 'sahla sandwich' in sandwich_orders:
        sandwich_orders.remove('sahla sandwich')
    else:
        activate=False

print(f'移除后的列表：{",".join(str(i)for i in sandwich_orders)}')