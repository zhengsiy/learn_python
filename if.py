cars=['benz','bmw','aodi']
Car=[]
for car in cars:
    if car == 'bmw':
        car_u=car.upper()
        Car.append(car_u)
    else:
        car_t=car.title()
        Car.append(car_t)
print(Car)


for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())


car='audi'
if car=="Audi":
    print(True)
else:
    print(False)


if 'benz' not in cars:
    print(True)
else:
    print(False)

'''
age=input('请输入你的年龄：')
if age >=str(int(18)):
    print('恭喜您，已获得投票资格')
else:
    print('不好意思，你还未满18岁，不能进行投票')'''

age=input('请输入你的年龄：')
ages=int(age)
if ages<=7:
    prince=10
elif ages<=18:
    prince=50
else:
    prince=65
print(f'你的们票价格是：{prince}')



