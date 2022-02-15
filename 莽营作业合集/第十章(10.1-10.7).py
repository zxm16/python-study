# 10.1python学习笔记


print('----------------10.1---------------')


file = 'unit10.txt'
with open(file) as file01:
    note = file01.read()
    print(note)
    # 打印读取整个文件
    for note03 in note:
        # 遍历文本里每一个元素
        print(note03)
print('------小题标志--------')
with open(file) as file02:
    note01 = file02.readlines()
    # 读取file01文件并且将其每行作为列表的每一项元素
    print(note01)
    for note02 in note01:
        # 遍历列表里的每一个元素
        print(note02.rsplit())
    # 打印遍历文件对象


print('----------------下一题---------------')


# 10.2 C语言 学习笔记


print('----------------10.2---------------')


message = 'i like you !'
# 定义一个字符串
message01 = message.replace('like', 'love')
# 用replace函数将message值改为需要的新值并且赋值给message01
print(message01)
# 打印更改过后的新值
with open('unit10.txt') as file03:
    note04 = file03.read()
    print(note04)
    note05 = note04.replace('python', 'C')
    print(note05)
    '''
    与上面的示例一样只不过这是调用文本来进行对文本进行更改
    '''


print('----------------下一题---------------')


# 10.3 访客


print('----------------10.3---------------')


file_user = 'user.txt'
# 创建一个文件名并将名字赋值给file_user
with open(file_user, 'w') as user01:
    # 先打开file_user因为没有创建这个文件，
    # 所以直接创建这个文件并且调用write模式向文件写入文本
    i = 1
    # 定义一个变量来做定次数的值

    while True:
        i += 1
        user_write = input('(输入exit进行退出)请输入你的姓名，地址：')
        # 将输入的赋值给user_write
        user01.write(f'{user_write}\n')
        # 将输入的文本写入text文件中
        if i >= 4:
            break
        elif user_write == 'exit':
            break
'''
设置循环体来向file_user中不断写入文件
'''

print('----------------下一题---------------')


# 10.4 访客


print('----------------10.4---------------')


file_user01 = 'guest_book.txt'
# 创建一个文件名并将名字赋值给file_user
with open(file_user01, 'w') as user02:
    # 先打开file_user因为没有创建这个文件，
    # 所以直接创建这个文件并且调用write模式向文件写入文本
    x = 1
    # 定义一个变量来做定次数的值

    while True:
        x += 1
        user_write01 = input('(输入exit进行退出)请输入你的姓名，地址：')
        # 将输入的赋值给user_write
        user02.write(f'{user_write01}\n')
        # 将输入的文本写入text文件中
        print(f'欢迎你{user_write01}')
        if x >= 4:
            break
        elif user_write == 'exit':
            break
'''
设置循环体来向file_user中不断写入文件
'''


print('----------------下一题---------------')


# 10.5 调查


print('----------------10.5---------------')
file_search = 'love.txt'
with open(file_search, 'w') as fs:
    i = 1

    while True:
        i += 1
        search_people = input('(输入exit退出写入)你喜欢什么能不能告诉我：')
        fs.write(f'{search_people}\n')
        if i >= 5:
            break
        elif search_people == 'exit':
            break

print('----------------下一题---------------')


# 10.6 加法运算


print('----------------10.6---------------')
print('请输入你想进行加法运算的两个数的数')
operation_number01 = input('第一个数')
# 将输入的值赋给operation_number01
operation_number02 = input('第一个数')
try:
    operation_plus = int(operation_number02) + int(operation_number01)
    # 将两个参数相加并且将参数化为长整型这样输入字符串就会报错
except ValueError:
    print('请输入数字而不是字！')
else:
    print(f'和为{operation_plus}')


print('----------------下一题---------------')


# 10.7 加法计算器


print('----------------10.7---------------')
while True:
    print('请输入你想进行加法运算的两个数的数(输入exit进行退出程序)')
    operation_number01 = input('第一个数')
    # 将输入的值赋给operation_number01
    if operation_number01 == 'exit':
        break
    operation_number02 = input('第二个数')
    if operation_number02 == 'exit':
        break

    try:
        operation_plus = int(operation_number02) + int(operation_number01)
        # 将两个参数相加并且将参数化为长整型这样输入字符串就会报错
    except ValueError:
        print('请输入数字而不是字！')
    else:
        print(f'和为{operation_plus}')
        '''
        退出程序操作
        '''


print('----------------下一题---------------')



