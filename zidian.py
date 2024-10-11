masagge={'name':'刘弘基','sex':'man','age':22,'position':'left'}
print(f"原始位置：{masagge['position']}")
if masagge['age']<=18:
    print(f"{masagge['name']}is a minor")
else:
    print(f"{masagge['name']}is a teenager")

#修改键值对中的内容
masagge['age']=masagge['age']+3
print(masagge['age'])
print(masagge)

#删除字典中的键值对
del masagge['position']
print(masagge)

favorite_languages={'yewezhi':'java','liujialong':'c','zhengsiyu':'python','lizhipeng':'ruby','liuongji':'php'}
language=favorite_languages['zhengsiyu'].title()
print(f"zhengsiyu's favorite language is {language}")


#遍历字典中的键值对（items（））
for name,language in favorite_languages.items():
    print(f'\nname:{name}')
    print(f'language:{language}')

#遍历字典中的所有键（keys（））
names=[]
for name in favorite_languages.keys():
    names.append(name)
print(f'调查的所有人为：{names}')

#遍历字典中的所有值（values（））
for language in favorite_languages.values():
    print(language.title())
 
#按特定顺序取出字典中的键:sorted()
for  languages in sorted(favorite_languages.values()):
    print(f'\nMy friends are like {languages.title()}')




#先剔除字典中的重复项，是集合中的元素独一无二  set()
favorite_fruits={'zhengsiyu':'apple','yeweizhi':'bannar','liuhongji':'orange','lizhipeng':'watermenlar','xinwang':'apple'}
for fruits in set(favorite_fruits.values()):
    print(fruits)




#先去重，再排序
differ_fruits=[]
for fruits in set(favorite_fruits.values()):
    differ_fruits.append(fruits)
print(sorted(differ_fruits))
    

#嵌套
#在列表中嵌套字典
aliens=[]     #创建一个空列表用于储存后面生成的新外星人
# 使用range（）函数创建30个外星人（从0到29进行遍历，每遍历一次将颜色和分数以及速度等信息赋值给new_alien）
for new_alien in range(30):
    new_alien={'color':'red','point':5,'speed':'slow'}
    aliens.append(new_alien)

#修改列表中的第四个元素的值

aliens[3]={'color': 'green', 'point': 10, 'speed': 'slow'}

#修改liens列表中的一些数据
for alien in aliens[:3]:
    if alien['color']=='red':
        alien['color']='green'
        alien['point']=10
        alien['speed']='medium'
    elif alien['color']=='green':
          alien['color']='yellow'
          alien['point']=15
          alien['speed']='fast'


#打印aliens列表中前5个外星人数据
for alien in aliens[:5]:
    print(alien)
#查看列表中元素的长度，确认是否添加成功
print(f'The total number of aliens:{len(aliens)}')



favorite_languages={'zhengsiyu':['c','php'],
                    'xinwang':['java','js'],
                    'lizhipeng':['python','ruby'],
                    'liuhongji':['c','python']}
for name,languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f'\t{language.title()}')
    
messages={'names':'zhengsiyu',
          'favorite_language':['c','php','python']}
print(f'{messages["names"]} like ')
for favor_lan in messages['favorite_language']:
    print(f'\t'+favor_lan)


users={'siyuzheng':{'firstname':'zheng','last_name':'siyu','location':'江西万载'},
       'hongjiliu':{'firstname':'liu','last_name':'hongji','location':'广东韶关'},
       'wangxin':{'firstname':'xin','last_name':'wang','location':'江西宜春'}}

wife=[]
hasband=[]
for username,user_info in users.items():
    print(f'\nUsername:{username}')
    Full_name=f"{user_info['firstname']}{user_info['last_name']}"
    Location=user_info['location']
    print(f'\tFull_name: {Full_name}')
    print(f'\tLocation: {Location}')
    
    if Full_name=='zhengsiyu':
        wife.append(Full_name)
    if Full_name=='xinwang':
        hasband.append(Full_name)
print(f"\n And 这是我第4次在test里面写的东西 s wife")



# 这是我第一次在test里面写的东西
