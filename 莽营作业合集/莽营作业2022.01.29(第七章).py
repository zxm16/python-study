# 7.1
print('-------7.1--------')
input("please input what's type do you like of the car: ")
# 提示输入自己喜欢car的种类
print("let me see if i can find you a subaru")
print('------------------下一题---------------------')


# 7.2
print('-------7.2--------')
number_eat = input('你们有多少个人需要用餐：')
number_eat = int(number_eat)
if number_eat >= 8:
    print('很抱歉我们这里没有多的空位了！')
else:
    print('预定成功!')
print('------------------下一题---------------------')


# 7.3
print('-------7.2--------')
number_number = input('please input multiple number of 20: ')
number_number = int(number_number)
if number_number % 20 == 0:
    print("this number is multiple of 20")
else:
    print("this number isn't multiple of 20")
print('------------------下一题---------------------')


# 7.4
print('-------7.4--------')
eat01 = '\n请输入你想要的披萨配料：'
eat01 += "\n（如果添加完毕请输入’0k‘来结束点餐）"
while True:
    eat_02 = input(eat01)
    # 将在eat01中键入的值赋给eat02
    # 来作为条件给if语句进行判断
    if eat_02 == 'ok':
        break
    # 用if语句来判断食客是否键入
    # ‘完成’来结束点餐
    print('添加完毕')
    # 当不会进入到if语句里时会一直显示
    # 它来提示添加的调料是成功的
print('点餐完毕，欢迎下次光临')
print('------------------下一题---------------------')


#7.5
print('-------7.5--------')
age_movie = '请先输入你的名字来进行购票'
age_movie += '\n你的年龄是：'
while True:
    # 给while赋True直接进入循环
    age_movie01 = int(input(age_movie))
    # 先将键入的字符串转换为数值
    # 再将转换的数值赋给age_n=movie来进行下面的if判断
    if age_movie01 < 3:
        print('因为年龄不到3岁所以不用收票')
    if age_movie01 >= 3 and age_movie01 < 12:
        print('本次收费为10美元')
    if age_movie01 >= 12:
        print('本次收费为15美元')
    # 以上代码都是进行对键入的值进行分层判断
    print('祝您有好的体验')
    break
    # 执行判断后直接跳出循环
print('------------------下一题---------------------')


# 7.6
print('-------7.6--------')
age_movie = '请先输入你的名字来进行购票'
age_movie += '\n你的年龄是：'
active = True
while active:
    age_movie01 = int(input(age_movie))
    if age_movie01 < 3:
        print('因为年龄不到3岁所以不用收票')
    if age_movie01 >= 3 and age_movie01 < 12:
        print('本次收费为10美元')
    if age_movie01 >= 12:
        print('本次收费为15美元')
    print('祝您有好的体验')
    break
print('------------------下一题---------------------')


# 7.7
print('-------7.7--------')
x = 1
while x <= 5:
    print("完了你要一直循环下去了快"
          "按Ctrl+F2来结束它！")
print('------------------下一题---------------------')


# 7.8
print('-------7.8--------')
sandwich_orders = ['水果三明治', '多肉三明治', '海鲜三明治']
finished_sandwich = []
while sandwich_orders:
    # 在sandwich中循环取值
    finished_sandwich01 = sandwich_orders.pop()
    # 将循环取的值进行弹出
    print(f'{finished_sandwich01}做好了！')
    finished_sandwich.append(finished_sandwich01)
    # 将弹出完成的三明治添加到已完成的列表中
print(finished_sandwich)
# 将已完成的三明治列表打印出来
print('------------------下一题---------------------')


# 7.9
print('-------7.9--------')
sandwich_orders01 = ['水果三明治', '多肉三明治', '海鲜三明治', '牛肉三明治', '牛肉三明治', '牛肉三明治']
print('牛肉三明治已经卖完了！')
while '牛肉三明治' in sandwich_orders01:
    sandwich_orders01.remove('牛肉三明治')
print(sandwich_orders01)
print('------------------下一题---------------------')

# 7.10
print('-------7.10--------')
visit_place = []
while True:
    visit_places = '如果有一次机会，你最想去的旅游地'
    visit_place.append(input(visit_places))
    print(visit_place)

print('------------------2022.01.28日python第7七章学习结束----------------------')
