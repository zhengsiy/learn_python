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
    print(f'调查的所有人为：{name}')
    names.append(name)
#print(f'调查的所有人为：{names}')

#遍历字典中的所有值（values（））
for language in favorite_languages.values():
    print(language.title())
 












