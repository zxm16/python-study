#5.1
car='吴磊'
print(car == '吴磊')
print('------------------下一题----------------------')
#5.2
name = 'Wulei'
name_01 = 'wulei'
print(name == name_01)
print(name != name_01)
print('------------------下一题----------------------')


#5.3
alien_color = 'red'
if 'red' in alien_color:
    print('player get 5 point!')
    if 'red' in alien_color:
        print('player get 10 point!')
#if 语句的初次使用
print('------------------下一题----------------------')
#5.4
if 'green' in alien_color:
    print('You kill the alien you get the 5 point!')
    if 'green' in alien_color:
        print('player get 10 point!')
#用if语句实现命令
if 'green' in alien_color:
    print('You kill the alien you get the 5 point！')
else:
    print('player get 10 point!')
#用if-else实现命令
print('------------------下一题---------------------')


#5.5
if 'green' in alien_color:
    print('player get 5 point!')
elif 'yellow' in alien_color:
    print('player get 10 point!')
else:
    print('player get 15 point！')
print('------------------下一题---------------------')


#5.6
age = 40
if age < 2:
    print('这个人是婴儿')
elif age >= 4 and age<4:
    print('这个人是幼儿')
elif age >= 4 and age <13:
    print('这个人是儿童')
elif age >= 13 and age < 20:
    print('这个人是青少年')
elif age >= 20 and age < 65:
    print('这个人是成年人')
else:
    print('这个人是老年人')
#通过if-elif-else来进行判断
print('------------------下一题---------------------')


#5.7
fruit=['banana', 'apple', 'pear']
if 'banana' in fruit:
    print('You really like banana!')
if 'apple' in fruit:
    print('You really like apple')
if 'pear' in fruit:
    print('You really like pear!')
#检查列表中的元素是否在列表中
print('------------------下一题---------------------')


#5.8
user = ['admin', 'mike', 'jodan', 'hans']
for user01 in user:
    if 'admin' in user01:
        print(f'Hello {user01},would you like to see a status report!')
    else:
        print(f'Hello {user01},thanks for logging in again!')
#先遍历在进行if语句进行判断分别输出不同的内容
print('------------------下一题---------------------')


#5.9
user02 = []
if user02:
    print('nice we have one more user！')
else:
    print('We need to find some user!')
print('------------------下一题---------------------')


#5.10
current_users = ['mike', 'jodan', 'hans', 'li', 'bili']
new_users = ['mike', 'Mike', 'fan', 'wu', 'nei']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('please use other name to logging')
    else:
        print('welcome to game ,you have been our member!')


print('------------------下一题---------------------')
#5.11
number_ordinals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number_ordinal in number_ordinals:
    if number_ordinal == 3:
        print(f'{number_ordinal}rd')
        continue
    if number_ordinal == 2:
        print(f'{number_ordinal}nd')
        continue
    else:
        print(f'{number_ordinal}st')
print('------------------下一题---------------------')

print('-------------------------------六章-------------------------------')

#6.1
print('--------6.1---------')
name_friend = {'firstname': '张', 'lastname': '吃饭', 'age': '23', 'city': '武汉'}
print(name_friend)
#创建一个字典
print('------------------下一题---------------------')


#6.2
print('--------6.2---------')
number_like = {'张吃饭': '2', '张睡觉': '3', '吴磊': '4', '张洗澡': '5'}
print(number_like)
#创建一个字典
print('------------------下一题---------------------')


#6.3
print('--------6.3---------')
pythons={'sort':'排序', 'pop': '弹出', 'append': '添加', 'insert': '插入', 'range': '创建随机数组'}
python=pythons['sort']
#用一般的方法来调用元组的值
print(f'sort的用法是：{python}')
python01=pythons.get('pop')
#用.get()的方法来调用元组的值
print(f'pop的用法是：{python01}')
print('------------------下一题---------------------')


# py={'sort':'排序','pop':'弹出','append':'添加','insert':'插入','range':'创建随机数组'}
# for name22 in py.keys():
#     print(f'{name22}')
# for name23 in py:
#     print(f'{name23}')
# for v,name24 in py.items():
#     print(f'{name24}')
#校验字典的遍历
#校验代码

#6.4
print('--------6.4---------')
for name24 in pythons.values():
    print(name24)
#获取元组的value
for name25 in pythons.keys():
    print(name25)
#获取元组的key
print('------------------下一题---------------------')


#6.5
print('--------6.5---------')
#6.5.1
river = {'黄河': '陕西', '长江': '武汉', '亚马孙河': '巴西'}
for river_name in river.keys():
    river_name01 = river_name
    river_city = river[river_name01]
    '''
    将得到的键给到寻找字典元素
     的方法中再将搜到的值赋给新的值.
    '''
    print(f'{river_name} 流过 {river_city}')
#6.5.2
for river_name in river.keys():
    print(river_name)
for river_city in river.values():
    print(river_city)
print('------------------下一题---------------------')


#6.6
print('--------6.6---------')
name_friend02 = {'firstname': '王', 'lastname': '睡觉', 'age': '21', 'city': '北京'}
name_friend01 = {'firstname': '李', 'lastname': '喝水', 'age': '22', 'city': '深圳'}
peoples = [name_friend,name_friend01,name_friend02]
#将字典存储在列表中
for people in peoples:
    print(people)
    #打印列表中的字典元素

print('------------------下一题---------------------')



#6.7
print('--------6.8---------')
bog = {'类型': '贵宾狗', '主人': 'bili'}
cat = {'类型': '英短', '主人': '张吃饭'}
pig = {'类型': '乳猪', '主人': '吴磊'}
pets = [bog, cat, pig]
for pet in pets:
    print(pet)
print('------------------下一题---------------------')


#6.9
print('--------6.9---------')
favorite_places = {'张吃饭': ['北京', '武汉', '上海', '深圳'],
                   '张睡觉': ['北京', '武汉', '上海', '深圳'],
                   '张喝水': ['北京', '武汉', '上海', '深圳']}
for favorite_place in favorite_places.items():
    print(favorite_place)
print('------------------下一题---------------------')


#6.10
print('--------6.10---------')
number_like01 = {'张吃饭': [1, 2], '张睡觉': [1, 2], '吴磊': [1, 2], '张洗澡': [1, 2]}
print(number_like01)
print('------------------下一题---------------------')


#6.11
print('--------6.11---------')
cities = {'武汉': {'国家': '中国', '人口': '1200w'},
          '上海': {'国家': '中国', '人口': '1200w'},
          '北京': {'国家': '中国', '人口': '1200w'}
          }
print(cities)
print('------------------2022.01.28日python学习结束---------------------')
