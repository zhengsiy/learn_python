def city_country(city,country,population=''):
    '''返回城市名和所属国家'''

#使population参数变成可选
    if population:

        message=f'{city} {country}-population {population}'
    else:
         message=f'{city} {country}'

    return message


print('Enter "q" at any time to quit.')
while True:
        city=input('请输入城市名：')
        if city  == 'q':
            break
        country=input('请输入该城市所属国家：')
        if country == 'q':
            break
        break

get_messages=city_country(city,country,population='')
print(f'\tNeattly get_messages:{get_messages}')
