#二章
#2.1
x=10
print(x)
#2.2
y=20
print(y)
z=y
print(z)
#2.3
message="Eric"
y=f"Hello {message},would you like to learn some python today?"
print(y)
#2.4
x='wangDan'
print(x.title())
print(x.upper())
print(x.lower())
#2.5
name='Albert Einstein'
massage=" once said,'A person who never made a mistake never tried anything new'"
email=f"{name}{massage}"
print(email)
#2.6
famous_person="张吃饭"
message01="'遇事不决铁锅炖自己'"
email01=f"{famous_person}说:{message01}"
print(email01)
'''
拼接f设置方法是通过将"{A}{B}"
中花括号的字符串拼接在一起达到
连成一个字符串的效果。
'''
#2.7
name01='张\n吃\n\t饭\n\t'#\t是加制表符\n是换行
print(name01)
#2.7(1)
name02=' 张吃饭  '
print(name02.rstrip())
print(name02.lstrip())
#2.8
print(3+4)
print(3-4)
print(3*4)
print(3/4)
#2.9
x=11
favorite_number='我最喜欢的数是：'
print(f'{favorite_number}{x}')
#2.10
#添加注释
x=11#定义变量1
favorite_number='我最喜欢的数是：'#定义变量2
print(f'{favorite_number}{x}')#将变量1和变量2拼接成一个字符串
#2.11
import this


#三章
#3.1
name_friend=['张吃饭','熊超','王亚楠','吴俊强','李伯平','韦经理','吴磊','张泽']
print(name_friend[0])
print(name_friend[1])
print(name_friend[2])
print(name_friend[3])
#3.2
email_name='很高兴认识你!'
print(f'{name_friend[1]}{email_name}')
print(f'{name_friend[2]}{email_name}')
print(f'{name_friend[3]}{email_name}')
#3.3
name_transport=['car','cycle','motorcycle']
print(f"i would like to own a {name_transport[0]} ")
print(f"i would like to own a {name_transport[1]} ")
print(f"i would like to own a {name_transport[2]} ")
#3.4
email_invite='我想邀请去实验室做实验'
print(f"我想邀请{name_friend[0]}去实验室做实验")
print(f"我想邀请{name_friend[1]}去实验室做实验")
print(f"我想邀请{name_friend[2]}去实验室做实验")
#3.5
print('熊超，张吃饭无法到')
name_friend[0]='郭老师'
name_friend[1]='朱老师'
print(name_friend)
print(f"我想邀请{name_friend[0]}去实验室做实验")
print(f"我想邀请{name_friend[1]}去实验室做实验")
#3.6
print('我找到更大的实验室了！')
name_friend.insert(0,'张吃饭')
name_friend.insert(3,'熊超')
name_friend.append('张鑫满')
print(name_friend)
print(len(name_friend))
print(f"我想邀请{name_friend[0]}去实验室做实验")
print(f"我想邀请{name_friend[1]}去实验室做实验")
print(f"我想邀请{name_friend[2]}去实验室做实验")
print(f"我想邀请{name_friend[3]}去实验室做实验")
print(f"我想邀请{name_friend[4]}去实验室做实验")
print(f"我想邀请{name_friend[5]}去实验室做实验")
print(f"我想邀请{name_friend[6]}去实验室做实验")
print(f"我想邀请{name_friend[7]}去实验室做实验")
print(f"我想邀请{name_friend[8]}去实验室做实验")
print(f"我想邀请{name_friend[9]}去实验室做实验")
print(f"我想邀请{name_friend[10]}去实验室做实验")
#3.7
print(name_friend)
#打印数数组元素
print('太遗憾了我只能和两位同志一起去做实验了')
name_del=name_friend.pop(0)
print(f'很抱歉不能邀请你了{name_del}')
name_del=name_friend.pop(0)
print(f'很抱歉不能邀请你了{name_del}')
name_del=name_friend.pop(0)
print(f'很抱歉不能邀请你了{name_del}')
name_del=name_friend.pop(0)
print(f'很抱歉不能邀请你了{name_del}')
name_del=name_friend.pop(0)
print(f'很抱歉不能邀请你了{name_del}')
name_del=name_friend.pop(0)
print(f'很抱歉不能邀请你了{name_del}')
name_del=name_friend.pop(0)
print(f'很抱歉不能邀请你了{name_del}')
name_del=name_friend.pop(0)
print(f'很抱歉不能邀请你了{name_del}')
name_del=name_friend.pop(0)
print(f'很抱歉不能邀请你了{name_del}')
#将数组的元素删除弹出并打印
print(name_friend)
#打印数组元素
print(len(name_friend))
#打印数组长度
name_last=name_friend[0]
print(f'我想和你去{name_last}')
name_last=name_friend[1]
print(f'我想和你去{name_last}')
#对最后两位进行邀请)
del name_friend[0]
#删除数组第一个元素
print(name_friend)
#打印数组的元素
del name_friend[0]
#删除数组第一个元素
print(name_friend)
#打印数组的元素
print(len(name_friend))
#打印数组的长度
#3.8
name_visit=['china','japan','german']
print(name_visit)
print(sorted(name_visit))
print(name_visit)
#按照字母顺序来临时排序数组元素
#name_visit.sorted(reverse=True)
print(name_visit)
#对数组进行临时倒序排序
name_visit.reverse()
print(name_visit)
#直接对数组进行倒序排列
name_visit.reverse()
print(name_visit)
#对数组进行恢复
name_visit.sort()
print(name_visit)
#用sort来排列数组永久改变
name_visit.sort(reverse=True)
print(name_visit)
#用sort来排列数组并且倒置永久改变
#3.9
print(len(name_friend))
#打印邀请朋友的人数
#3.10
name_shoes=['nike','adidas','Anta','lining']
name_shoes.append('361')
print(name_shoes)
#增
name_shoes.pop(4)
print(name_shoes)
del name_shoes[0]
print(name_shoes)
#删
name_shoes.insert(0,'nike')
print(name_shoes)
#插
print(sorted(name_shoes))
print(name_shoes)
name_shoes.sort()
print(name_shoes)
name_shoes.reverse()
print(name_shoes)
# print(sorted(name_shoes.reverse()))
name_shoes.reverse()
print(name_shoes)
#3.11
# print(name_shoes[4])
# 当索引错误时出现的错误


#四章
# 4.1
pizzas=['培根','鸡肉','水果']
for pizza in pizzas:
    print(pizza)
    #输出循环的元素
for pizza in pizzas:
    print(f'我喜欢{pizza}披萨')
    #将循环的内容进行字符串拼接
print('这些披萨我都喜欢！')
#4.2
name_animals=['dog','cat','rabbit']
for name_animal in name_animals:
    print(f'a {name_animal} would make a great pet!')
    print('Any of these animals would make a great pet')
#4.3
number01=range(1,21)
for number011 in number01:
    print(number011)
#随机生成20个数并实验for循环进行打印
#4.4
number02=range(1,1000001)
for number021 in number02:
    print(number021)
#随机生成100000个数并答应
#4.5
number03=[1,2,3,4,5,6]
print(min(number03))
print(max(number03))
print(sum(number03))
#输出数组中最小，最大，所有元素的和
#4.6
number04=list(range(1,21,2))
print(number04)
#生成奇数的数组并打印出他们
#4.7
number05=list(range(3,31,3))
for number051 in number05:
    print(number051)
#生成可以被3整除的数组
#4.8
number06=[value**3 for value in range(1,11)]
print(number06)
#生成一个以（1-10）的三次方的数组
#4.9
number07=[value1**2 for value1 in range(1,11)]
print(number07)
#用解析列表生成1-10立方的数组
#4.10
number08=number03[:3]
for number081 in number08:
    print(f'The first three item in the list are:{number081}')
#取前三个元素
number08=number03[2:4]
for number081 in number08:
    print(f'The middle two item in the list are:{number081}')
#取中间的两个元素
number08=number03[2:]
for number081 in number08:
    print(f'The last four item in the list are:{number081}')
#取最后的两个元素
# 4.11
pizza01=pizzas[:]
#遍历pizzas的元素并且将元素赋值给pizza01
pizza01.append('海鲜')
#向pizza01中添加新元素
print(pizza01)
for pizza011 in pizza01:
    print(f'我朋友喜欢{pizza}披萨')
for pizza in pizzas:
    print(f'我喜欢{pizza}披萨')
#4.12
car_name=['法拉利','迈凯伦','柯尼塞格']
car_speed=['500','700','800']
for car_name01 in car_name:
    print(f'这个车的名字是{car_name01}')
for car_speed01 in car_speed:
    print(f'这个车的速度是{car_speed01}')
#4.13
food=('鱼香肉丝','糖醋里脊','番茄鸡蛋')
for food01 in food:
    print(food01)
    #打印每一种食物
# food[0]='www'
#元组不允许修改元素
food=('宫爆鸡丁','糖醋里脊','番茄鸡蛋')
for food01 in food:
    print(food01)
#修改元组元素
