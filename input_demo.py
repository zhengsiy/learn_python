#输入 :input（）
#name=input('请输入名字：')   # 阻塞式:未输入则开启阻塞模式，输入内容回车后流通，将输入的内容赋值给变量name
#print(name)

#input键盘输入的都是字符串类型，即使输入的是整数，也会自动添加引号成为字符串类型
#coins=input('请充值：')
#print(type(coins))



# 练习
name=input('请输入你的用户名：')

print('''
**************************
     欢迎来到英雄联盟
**************************
''')

item=input('请输入要购买的装备：')
coins=input('请输入你要充值的金额：')
#print(f'{name}拥有{item}装备，花了{coins}钱')
print('%s拥有%s装备，花了%s钱' %(name,item,coins))

