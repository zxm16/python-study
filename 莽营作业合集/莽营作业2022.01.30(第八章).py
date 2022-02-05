# 8.1
def display_message():
    print('本章第一部分学习了如何创建一个函数什么是实参什么是形参')

display_message()
# 调用函数
print('------------------下一题---------------------')


# 8.2
print('-------8.2--------')
def favorite_book(title):
    # 定义一个函数并且给他赋一个形参即：title
    print(f'one of my favorite books is {title}')
    # 调用形参并且将其打印出来

favorite_book('Alice in wonderland')
# 给形参title赋值一个实参并且返回到函数中调用
'''
犯的错误有：1.单独给形参赋值比如title = 'Alice in wonderland'
            这是没有必要的只需要在调用函数的时候给他传递实参就行了！
'''
print('------------------下一题---------------------')


# 8.3
print('-------8.3--------')
def make_shirt(size, icon):
    print(f'你想要{size}码的的短袖')
    print(f'我想要一个{icon}logo的短袖')

make_shirt('L', 'HUAWEI')
'''
前面一个实参对应的是第一个形参，第二个实参就对应着第二个形参.
因为实参不是位置指定实所以按照位置实参来对照来赋值的
'''
print('------------------下一题---------------------')


# 8.4
print('-------8.4--------')
def make_shirt01(size01, icon01='I love python'):
    print(f'你想要{size01}码的的短袖')
    print(f'我想要一个{icon01}logo的短袖')

make_shirt01('L')
make_shirt01('M', "'HUAWEI'")
print('------------------下一题---------------------')


# 8.5
print('-------8.5--------')
def describe_city(name = '武汉', country = '中国'):
    print(f'{name}在{country}')

describe_city()
describe_city('重庆')
describe_city(name='华盛顿', country='美国')
describe_city('巴黎', country='法国')
describe_city('纽约', '美国')
"""
describe_city(name='华盛顿', '美国')
这句话不能行当name指定华盛顿后country变成第一个
形参而后面的美国是第二个实参所以不能赋值并且报错
"""
print('------------------下一题---------------------')


# 8.6
print('-------8.6--------')
def city_country(name, country):
    country_palce = print(f'{name},{country}')
    return country_palce

city_country('武汉', '中国')
city_country('巴黎', '法国')
city_country('柏林', '德国')
print('------------------下一题---------------------')


# 8.7
print('-------8.7.1--------')
while True:
    print("登记结束或直接退出请按exit")
    singer_name = input('这位歌手的名字是：')
    if singer_name == 'exit':
        break
    album_name = input('这部专辑的名字是：')
    if album_name == 'exit':
        break
    def make_album(singer, name):
        person = {'歌手': singer, '专辑名': name}
        print(person)
        return person

    make_album(singer_name, album_name)

print('-------8.7.2--------')
while True:
    singer_name = input('这位歌手的名字是：')
    if singer_name == 'exit':
        break
    album_name = input('这部专辑的名字是：')
    if album_name == 'exit':
        break
    album_name_number = int(input('这部有多少曲：'))
    if album_name_number == 'exit':
        break
    def make_album(singer, name, album_name_number = None):
        person = {'歌手': singer, '专辑名': name, '曲数': album_name_number}
        print(person)
        return person

    make_album(singer_name, album_name, album_name_number)
print('------------------下一题---------------------')


# 8.8
print('-------8.8--------')
while True:
    singer_name = input('这位歌手的名字是：')
    if singer_name == 'exit':
        break
    album_name = input('这部专辑的名字是：')
    if album_name == 'exit':
        break
    album_name_number = int(input('这部有多少曲：'))
    if album_name_number == 'exit':
        break
    def make_album(singer, name, album_name_number = None):
        person = {'歌手': singer, '专辑名': name, '曲数': album_name_number}
        print(person)
        return person

    make_album(singer_name, album_name, album_name_number)
print('------------------下一题---------------------')


# 8.9
print('-------8.9--------')
name_information = ['你好', '我是', '张吃饭']
def showmessage(show):
    for show1 in show:
        print(show1)

showmessage(name_information)
print('------------------下一题---------------------')


# 8.10
print('-------8.10--------')
name_information = ['你好', '我是', '张吃饭']
send_message = []
def showmessage(show):
    for show1 in show:
        print(show1)
        send_message.append(show1)

showmessage(name_information)
print(name_information)
print(send_message)
print('------------------下一题---------------------')


# 8.11
print('-------8.11--------')
name_information = ['你好', '我是', '张吃饭']
send_message = []
def showmessage(show):
    for show1 in show:
        print(show1)
        send_message.append(show1)

showmessage(name_information)
print(name_information)
print(send_message)
print('------------------下一题---------------------')


# 8.12
print('-------8.12--------')
def pizza(*food):
    print('你想要的配料有：')
    for food01 in food:
        print(f'-{food01}')

pizza('培根','海鲜','水果')
print('------------------下一题---------------------')


# 8.13
print('-------8.13--------')
name_information = ['鑫满', '张']
def build_profile(myself):
    i = 1
    while True:
        i = i + 1
        if i == 2:
            name_message = myself.pop()
            print(f'我姓：{name_message}')
        elif i == 3:
            name_message = myself.pop()
            print(f'我叫：{name_message}')
        elif i > 3:
            break

build_profile(name_information)
print('------------------下一题---------------------')


# 8.14
print('-------8.14--------')
def make_car(name, color, **car):
    car['car_name'] = name
    car['car_color'] = color
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
print('------------------2022.02.05日python第八章第一部分学习结束----------------------')


