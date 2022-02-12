# 9.1 餐馆
print('-------9-1-----------')


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f'打印{self.name}')

    def open_restaurant(self):
        print(f'打印{self.type}')

    def user_want(self):
        print(f'祁诗瑞想在{self.name}吃{self.type}')


my_restaurant = Restaurant('熊家里', '熊餐')
# 给类里的方法赋值
my_restaurant.describe_restaurant()
# 通过‘.’来调用describe的值
my_restaurant.open_restaurant()
# 通过‘.’来调用open的值
my_restaurant.user_want()
print('-----------------下一题------------------------')


# 9.2 两家餐馆
print('-------9-2-----------')


class Restaurant:
    def __init__(self, name, type01):
        self.name = name
        self.type = type01

    def describe_restaurant(self):
        print(f'打印{self.name}')

    def open_restaurant(self):
        print(f'打印{self.type}')


my_restaurant = Restaurant('kfc', 'potato01')
your_restaurant = Restaurant('mcdonald', 'potato')
# 给类里的方法赋值
print(f'my restaurant is {my_restaurant.name}')
print(f'my most like food is {my_restaurant.type}')

print(f'my restaurant is {your_restaurant.name}')
print(f'my most like food is {your_restaurant.type}')
print('-----------------下一题------------------------')


# 9.3 用户
print('-------9-3-----------')


class User:

    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name
        # 创建实例的方法

    def describe(self):
        print(f'{self.fn}')
        print(f'{self.ln}')
        # 定义方法

    def great_user(self):
        print(f'您好{self.fn}{self.ln}')
        # 定义方法


my_name01 = User('张', '鑫满')
my_name02 = User('李', '伯平')
my_name03 = User('韦', '梓渝')
# 将类的值赋值给变量

print(f'{my_name01.fn}{my_name01.ln}')
print(f'{my_name02.fn}{my_name02.ln}')
print(f'{my_name03.fn}{my_name03.ln}')
# 打印题目的需求
print('-----------------下一题------------------------')


# 9.4 就餐人数
print('-----------9-4-----------')


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.serverd_number = 0
        # 给变量self.serverd_number赋一个初始值

    def describe_restaurant(self):
        print(f'打印{self.name}')

    def open_restaurant(self):
        print(f'打印{self.type}')

    def set_number_served(self, people):
        self.serverd_number = people
        # 定义一个方法将实参传给形参的值赋值给变量self.serverd_number

    def increment_number_served(self, people01):
        self.serverd_number += people01
        # 定义一个方法进行对人数的增加

    def number_served(self):
        print(f'这有{self.serverd_number}个人在这里用餐')
        '''
        这里如果调用number_served（）方法就会将传给set_number_served（）的实参
        打印出来
        '''


my_restaurant = Restaurant('kfc', 'potato02')
# 给定Restaurant类实参，将Restaurant类赋值给变量my_restaurant

print(f'你想点的是{my_restaurant.name}{my_restaurant.type}')
# 调用方法中定义的name和type值直接调用

my_restaurant.set_number_served(23)
# 调用方法给set_number_served（）方法赋值一个实参

my_restaurant.number_served()
# 调用方法number_served（）将得到的结果打印出来

my_restaurant.increment_number_served(100)
# 调用方法给increment_number_served（）方法赋值一个实参

my_restaurant.number_served()
# 调用方法number_served（）将得到的结果打印出来
print('-----------------下一题------------------------')


# 9.5 尝试登录次数
print('-----------9-5-----------')


class User:

    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name
        self.login_attempt = 0
        # 创建实例的方法

    def describe(self):
        print(f'{self.fn}')
        print(f'{self.ln}')
        # 定义方法

    def great_user(self):
        print(f'您好{self.fn}{self.ln}')
        # 定义方法

    def login_time(self, time):
        self.login_attempt = time

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0

    def login_times_print(self):
        print(f'有{self.login_attempt}人次浏览了用户信息')


my_name01 = User('张', '鑫满')
my_name02 = User('李', '伯平')
my_name03 = User('韦', '梓渝')
# 将类的值赋值给变量
my_name01.great_user()
my_name02.great_user()
my_name03.great_user()
# 调用方法

print('---小题分界线---')
my_name03.login_time(20)
# 给属性self.login_attempt赋实参即给它赋值
my_name03.login_times_print()
# 将属性self.login_attempt的值打印出来
'''
赋值给属性并且将其打印出来看结果
'''

print('---小题分界线---')
my_name03.increment_login_attempts()
# 将属性self.login_attempt的值加1
my_name03.login_times_print()
# 将属性self.login_attempt的值打印出来
my_name03.increment_login_attempts()
# 同理
my_name03.login_times_print()
# 同理
my_name03.increment_login_attempts()
# 同理
my_name03.login_times_print()
# 同理
my_name03.increment_login_attempts()
# 同理
my_name03.login_times_print()
# 同理
my_name03.increment_login_attempts()
# 同理
my_name03.login_times_print()
# 同理
'''
将属性值进行累加加一次打印一次观察其的变化
'''

print('---小题分界线---')
my_name03.reset_login_attempts()
# 将属性self.login_attempt的值归零
my_name03.login_times_print()
# 将归零后的结果打印出来
'''
调用reset_login_attempts（）方法将属性
self.login_attempt的值归零即给它赋值0
'''
print('-----------------下一题------------------------')


# 9.6 冰淇凌小店
print('-----------9-6-----------')


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.serverd_number = 0
        # 给变量self.serverd_number赋一个初始值

    def describe_restaurant(self):
        print(f'打印{self.name}')

    def open_restaurant(self):
        print(f'打印{self.type}')

    def set_number_served(self, people):
        self.serverd_number = people
        # 定义一个方法将实参传给形参的值赋值给变量self.serverd_number

    def increment_number_served(self, people01):
        self.serverd_number += people01
        # 定义一个方法进行对人数的增加

    def number_served(self):
        print(f'这有{self.serverd_number}个人在这里用餐')
        '''
        这里如果调用number_served（）方法就会将传给set_number_served（）的实参
        打印出来
        '''


class IceCream(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        '''
        定义一个新类icecream，将这个新类作为Restaurant的子类
        首先初始化父类，然后通过super（）函数来来调用父类的方法
        '''


my_icecream = IceCream('kfc', 'sweet')
print(my_icecream.describe_restaurant())
print(my_icecream.open_restaurant())
print('-----------------下一题------------------------')


# 9.7 管理员
print('-----------9-7-----------')


class User:

    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name
        # 创建实例的方法
        # 创建一个属性login_attempt

    def describe(self):
        print(f'{self.fn}')
        print(f'{self.ln}')
        # 定义方法：显示管理员的名字以及姓名

    def great_user(self):
        print(f'您好{self.fn}{self.ln}')
        # 定义方法：对管理员发送问候语


class Admin(User):

    def __init__(self,  first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []

    def admin_name(self, power):
        self.privileges.append(power)

    def printf_admin(self):
        print(self.privileges)

    def printf_admin_name(self):
        print(f'欢迎你管理员：{self.fn}{self.ln}')


admin = Admin('张', '吃饭')
admin.printf_admin_name()
# 打印管理员的姓名并且欢迎管理员的进入系统
print('---小题分界线---')
admin.printf_admin()
admin.admin_name('你可以添加这个')
admin.printf_admin()
admin.admin_name('你可以删除这个')
admin.printf_admin()
admin.admin_name('你可以移动那个')
admin.printf_admin()
print('-----------------下一题------------------------')


# 9.8 权限
print('-----------9-8-----------')


class UserPower:

    def __init__(self, firstname, lastname):
        self.FirstName = firstname
        self.LastName = lastname

    def write_hello_user(self):
        print(f"Hello{self.FirstName}{self.LastName}! welcome to the python world!")


class AdminPower(UserPower):

    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.adminer = Privileges()
        '''
        1.super()来初始化父类要求后面的形参得和父类的形参相同
        2.self.adminer = Privileges()是用来将实例作为属性即创建一个新的类来
          创造的新类作为其属性进行调用
        '''

    def print_hello_admin(self):
        print(f"Hello{self.FirstName}{self.LastName}! welcome to the python world!")


class Privileges:

    def __init__(self, pop_admin_power=0):
        self.privileges = []
        self.PopAdminPower = pop_admin_power
        """
        1.定义self.privileges元数的初始值是一个列表
        2.因为要继承AdminPower类的属性得赋初值给形参
        所以需要给他赋一个初值，因为后面要继续使用并且
        要给它赋值所以其初值是什么都可以
        """

    def admin_name(self, admin_power):
        self.privileges.append(admin_power)
        '''
        将给的实参通过形参赋值给self.privileges
        因为self.privileges实列表所以用append
        来添加实参的元素
        
        '''

    def admin_name01(self):
        print(self.privileges)
        '''
        对列表进行打印
        '''

    def admin_name03(self):
        while True:
            self.PopAdminPower = self.privileges.pop()
            print(f'你可以执行这些权利{self.PopAdminPower}')
            '''
             对已经生成的列表的每一个元素进行弹出
            并将这些元数进行与字符串进行打印
            '''


AdminPower01 = AdminPower('张', '鑫满')
AdminPower01.print_hello_admin()
# 调用打印管理员名字的方法
print('---小题分界线---')
AdminPower01.adminer.admin_name('你可以添加这个')
# 执行admin_name方法，向列表添加元素
AdminPower01.adminer.admin_name01()
# 执行admin_name01方法，打印这个列表
AdminPower01.adminer.admin_name('你可以删除这个')
# 执行admin_name方法，向列表添加元素
AdminPower01.adminer.admin_name01()
AdminPower01.adminer.admin_name('你可以移动那个')
AdminPower01.adminer.admin_name01()
AdminPower01.adminer.admin_name03()
# 执行admin_name03将列表里每一个元素进行与字符串结合打印出来
print('-----------------下一题------------------------')


# 9.9 电瓶升级
print('-----------9-9-----------')


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year}{self.make}{self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it!')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battery = Battery

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f'This car has a {self.battery_size}-kwh battery-kwh battery')

    def fill_gas_tank(self):
        """打印电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=75):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print(f'This car has a {self.battery_size}-kwh battery')


print('-----------------下一题------------------------')
