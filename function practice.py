#P117
def display_message():
    print('本章节所学内容是函数，是整本书中最重要的内容')
display_message()

def favorate_book(title):
    print(f'\nOne of my favorite books is {title}!')
favorate_book('Alice in wonderland')


#122
def make_shirt(size,simple):
    '''T-shirt 信息'''
    print(f'\nMy T—shirt size is {size}')
    print(f'And i would like to have {simple} in reverse')
make_shirt('M','LOVE YOU')
make_shirt(simple='LOVE YOU',size='S')

def make_shirt(size='L',simple='I love python'):
    '''T-shirt 信息'''
    print(f'\nMy T—shirt size is {size}')
    print(f'And i would like to have {simple} in reverse')
make_shirt()
make_shirt('M')
make_shirt(simple='yes yes')


def describe_city(city_name,country='China'):
    print(f'\n{city_name} is in {country}')
describe_city('shanghai'.title())
describe_city(city_name='shezhen'.title())
describe_city('london'.title(),'britain'.title())


#127
def city_country(city,country):
    message={'city':city,'country':country}
    return message
    
musician=city_country('shanghai','China')
print(musician)


def make_album(singger_name,album_name,num=None):
    message={'singger_name':singger_name,'album_name':album_name}
    if num:
        message['num']=num
    return message
while True:
    print('\n请输入你最喜爱的歌手名和专辑名，按“q”可随时退出程序！')
    singger_name=input('你最喜欢的歌手是：')
    if singger_name=='q':
        break
    album_name=input('ta最出名的专辑是：')
    if album_name=='q':
        break
    musician=make_album(singger_name,album_name)
    print(musician)



'''
musician=make_album('周杰伦','稻香')
print(musician)
musician=make_album('张杰','这就是爱',3)
print(musician)
musician=make_album('大张伟','喜刷刷')
print(musician)
'''
#131
list=['苹果','橙子','橘子','西瓜']
def show_messages(texts):
    for text in texts:
        message=f'我喜欢吃{text}'
        print(message)
show_messages(list[:])

#print(list)

sent_messages=[]
def send_messages(texts):
    while list:
        message=list.pop()
        message=f'我喜欢吃{message}'
        sent_messages.append(message)
send_messages(list[:])

def have_send_messages(sent_messages):
    for send_message in sent_messages:
        print(f'\n以下是已经打印好的信息：{send_message}')

have_send_messages(sent_messages)

print(list)
print(sent_messages)


#134
def order_info(size,*toppings):
    print(f"\nmaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(topping)

order_info(16,'mushroom','chess')
order_info(13,'beef','chiken','poke','bancon')



def build_profile(fistname,lastname,**user_info):
    user_info['firstname']=fistname
    user_info['lastname']=lastname
    print(user_info)
build_profile('zheng','siyu',age='23',sex='girl',profess='student')


def cars_info(manufacturer,model,**other_info):
    other_info['manufacturer']=manufacturer
    other_info['model']=model
    return other_info
cars=cars_info('subaru','outback',color='bule',tow_package=True)
print(cars)
    


