#name = input ('Please tell me your name:')
#print(name)



#prompt='xinwang will be my hasband,and i love him forever.i am glad to be marry him'
#prompt += 'xinwang,will you marry me? Tell me you answer:'
#answer=input(prompt)
#print(f'\n{answer}')


#age=input('enter your age:')
#age=int(age)
#print(type(age))

'''
height=input('tell me your height:')
height=int(height)
if height <100:
    print('\n you are not tall enough to ride!')
elif 100<=height<=190:
    print('\n you are tall enough to ride!')
else:
    print('your are too tall to ride!')

#判断奇偶数
if height % 2 ==0:
    print(f'\n The number {height} is even.')
else:
    print(f'\n The number {height} is odd.')
'''



current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1





#prompt='xinwang will be my hasband,and i love him forever.i am glad to be marry him,will you marry me? Tell me you answer'
#prompt += '\nenter the "quit" to end the answer:'
#answer=''
#while answer !='quit':
#    answer=input(prompt)
#    if answer != 'quit':
#        print(answer)




prompt='Tell me something,and i will repeat it back to you:'
prompt += 'Enter "quit" to end the program.'
message=''
'''while message!='quit':
    message=input(prompt)
    if message!='quit':
        print(message)
'''

#使用标志
active=True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)


#使用break退出循环
prompt_city='\n Please enter the name of a city you have visitied:'
prompt_city +='\n (enter "quit" when you are finished.)'

active=True
while active:
    message=input(prompt_city)
    if message=='quit':
        break
    print(message)

#在循环中使用continue
current_number=-1
while current_number<=10:
    current_number+=1
    if current_number%2!=0:
        continue
    else:
        print(current_number)
    


#列表之间移动元素
unconfired_users=['linda','buruce','nancy']
confired_users=[]
while unconfired_users:
    confired_user=unconfired_users.pop()
    print(f'\nVerifying user : {confired_user}')
    confired_users.append(confired_user)

new_confired_users=','.join(str(i) for i in confired_users)

print(f'the following users have been confired:{new_confired_users.title()}')


#删除为特定值的所有元素
pets=['dog','cat','dog','glodfish','cat','rabbit','cat']
print(f'原始宠物数据：{",".join(str(i) for i in pets)}')

while 'cat' in pets:
    pets.remove('cat')

print(f'修改后宠物数据：{",".join(str(i) for i in pets)}')


#使用用户输入来填充字典
responses={}   #先创建一个空字典来储存后面输入的回答内容
polling_active=True    #创建一个标志，当polling_activa的值为True时，进入下面的while循环
while polling_active:
    name=input('what is your name:')    #调查名字
    response=input('which mountain would you like to clibe someday?')    #调查喜欢爬的山
    responses[name]=response    #将调查中的回答内容储存在最开始新建的空字典中

    repeat=input('wonld you like to let another person respond?(yes/no)')  #询问用户是否继续调查，回答yes即重新回到while循环中，回答no则结束while循环
    if repeat=='no':
        polling_active=False

print(f'\n---------polling results-----------')
for name,response in responses.items():                      #打印字典中的结果
    print(f"{name} would like to clibe {response}")



