#text = "你好,欢迎来到深圳"
#print(text)

#text="你好,欢迎来到nanchang "
#print(text)

#name = "hfalfk faeof"
#print(name.upper())

#name="SDJFA"
#print(name.lower())

#first_name="zheng"
#last_name="siyu"
#full_name=f"{first_name}{last_name}"
#print(f"Hello,{full_name.title()}")

#first_name="liu"
#last_name="jialong"
#full_name=f"{first_name} {last_name}"
#print(f"hello,{full_name.title()}")


#first_name="li"
#last_name="zhipeng"
#full_name=f"{first_name} {last_name}"
#print(f"你好，{full_name.title()}")



#first_name="liu"
#last_name="hongji"
#full_name=f"{first_name}{last_name}"
#print(f"hello,{full_name.title()}")
#print(f"\thello,{full_name.title()}")
#print(f"\thello,\n\t{full_name.title()}")

#language=' python ' 
#langua=language.strip()
#print(langua)

#message="my name's zhengsiyu"
#print(message)

#first_name="zheng"
#last_name="siyu"
#message='''"A person who made a mistake never tried anything new"'''
#print (f"{first_name.title()}{last_name} once said,\n{message}")

#print(2+3)
#print(2**3)
#print( 2 ** 3)
#print(140_000_000_000)


#print(3+5)
#print(10-2)
#print(2*4)
#print(16/2)

#全大写变量名通常用来表示一个常量，这个常数是不变的
#NUMBER=6
#print(f"My favorate nmber is {NUMBER}")

#python 之禅：即编写优秀代码的指导原则
#import this 

'''
first_name="zheng"
last_name="siyu"
message=f"亲爱的{first_name.title()}{last_name},\n\t请点击链接激活用户：激活用户"
print(message)

print("hello,py\\thon")
print(r'py\thon')
'''
'''
name='赵飞'
addres='深圳市宝安区轻铁锡花园'
number='18046653170'
num=3
#print('收货人：%s 收货地址：%s  联系方式：%s 数量：%s'  %(name,addres,number,num))
#print('收货人：'+name +' 收货地址：'+addres+' 联系方式'+number)


movie='大侦探皮卡丘'
ticket=45.9
count=35
total=ticket*count
print('电影：%s \n人数:%s \n单价:%.1f \n总票价:%.1f' %(movie,count,ticket,total))
'''
#message=input("你的名字：")

#print(f'所以你的名字叫：{message}')


num=[3,7,4,8,2,9,0]
#在列表末尾添加元素，使用append只能添加至末尾，且不能指定位置：在末尾添加1这个元素
num.append(1)
#使用insert可进行指定位置插入，逗号前规定索引的位置，后面规定要插入的值
num.insert(1,'zsy')
#改值，将原列表的索引为0的值改为'whh'
num[0]='whh'
#删除元素 del、pop（）、remove()
del num[-2]  #del 若知道其索引位置可删除任意位置的元素，删除后不能使用了该元素

num.pop()    #pop() 括号中不填写索引值则默认删除列表末尾最后一个元素，并且能够继续使用该元素;
num.pop(2)   #若在括号中填写索引值，则删除该索引位置的值
new_num=num.pop(2)    #若要继续使用该元素，则可以将要删除的值赋值给一个新的变量再使用

unuse=9
num.remove(unuse)  #不知道删除的的值所在位置，只知道要删除的元素的值，要接着使用该值，需要先把这个值赋值给一个新变量

print(num,unuse)





# 使用sort（）对列表进行排序，该排序方法使用后会改变原列表中的顺序且无法恢复到原来的顺序
#当列表中全是字符串时，则按字母顺序来排序；当列表中全是数字时，则按数字大小进行排序；
# 当列表中既有数字又有字符串时则无发使用该排序方法
list=['apple','orange','bannar','grepe','candy','dinner']
list.sort()
list.sort(reverse=True)
print(list)

list=[2,8,6]
list.sort()
print(list)
'''
list=[5,2,4,'bannar',0,'apple']
list.sort()
print(list)'''

# 使用sorted（）对列表中的元素进行排序，不改变原列表中的顺序，只是按排序后的顺序打印出来
# sorted（）使用方法：将原列表的变量名放到（列表变量名,reverse=true参数）
list=['apple','orange','bannar','grepe','candy','dinner']
new_list=sorted(list,reverse=True)
print(list)
print(new_list)

# reverse()永久性的修改元素列表的排列顺序，且只是反转原列表元素的排列顺序，若不使用sort、sorted排序则不会先进行排序
list.reverse()
print(list)

# 计算一个列表中有多少个值，可以使用len()函数
print(len(list),end='\n')


'''
fovrate_areas=['xi an','si chuang','chong qin','yun nan','bei jing']
for area in fovrate_areas:
    print(f'我最喜欢的城市是{area.title()}')
    print(f'期待下次再次来到{area.title()}.\n')
print('这就是我的旅游计划')'''


#for value in range(1,11,2):
#    print(value)


#numbers=list(range(1,21))
#print(numbers)

'''
list=[]   #创建一个空列表
for list_1 in range(1,21):      #将range函数中的数字一次取出，并将其与list_1这个变量关联
    print(f'这次取出的数字为：{list_1}')
    list.append(list_1)   #将每次从range函数中取出的关联了list_1的值添加到list这个空列表中去
print(list)       #最后将这个列表打印出来
'''

numbers=[]
for number in range(1,6):
    numbers.append(number**2)
print(numbers)


numbers=[]
for number in range(1,7):
    value=number**2
    numbers.append(value)
print(numbers)
print(min(numbers),max(numbers),sum(numbers))

#列表解析，将for循环和创建新元素的代码合并成一行，并自动附加新元素
numbers=[number**2 for number in range(1,5)]
print(numbers)


#切片处理，表示取出cubes列表中第1个到第9个的值，且设置步长为3，即第一个数取列表中的第一个值，第二个数取列表中的第个值
#print(cubes[0:10:3])
cubes=[1,4,6,2,5,7,3]
num=[]
for cube in cubes[0:3]:
    num.append(cube)
print(num)

#列表解析方式
#方式一：list_1=[cube for cube in cubes[0:4]]
#        print（list_1）

#方式二：print([cube for cube in cubes[0:4]])      这个中括号是必须的，否则生成不了列表












