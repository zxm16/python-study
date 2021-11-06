# 首字母变成大写的用法
name='joker'
print("姓名首字母转换大写%s"%name.capitalize())
pass


#去除字符串两侧的空格
a='   joker    '
b=a.strip()
print(b)
pass


#指定去除左或右的空格
a='   joker    '
print(a.lstrip())#删除左边的空格
pass

a='   joker    '
print(a.rstrip())#删除右边的空格
pass


#复制一个字符串
a='DAWALIXI'
print('a的内存地址%d'%id(a))#id函数可以查看内存地址。
b=a
print('b的内存地址%d'%id(b))#在复制操作后我们可以看到a，b的地址是一个地址。
print(b)
pass


#查找一个值是否存在于此字符串
#find查找
dataStr='I love python'
print(dataStr.find('y'))
#输出结果为8，即字符所在的位置为这一串字符串中的第8个（下标值），当没有在字符串中找到结果返回值为-1。
# （如果字符串中出现多个所需寻找的元素，+那么只能输出其首先查找到元素的位置！！！）
pass


#index查找
dataStr='I love python'
print(dataStr.index('n'))
#index查找基本与find查找一样，但index查找找不到元素时不同于find的找不到回输出 -1 index会直接报错。
pass


#判断一串字符串以~~元素开始/结束,判断完后输出结果为True或者False。
dataStr='I love python'
print(dataStr.startswith("I"))#判断字符串是否以“I”结尾，结果不是输出结果为Ture。
pass

dataStr='I love python'
print(dataStr.endswith("s"))#判断字符串是否以“s”结尾，结果不是输出结果为False。
pass


#大小写的转换（全部转换即整体转换）
dataStr='I love python'
print(dataStr.lower())#转换为小写
pass

dataStr='I love python'
print(dataStr.upper())#转换为大写
pass


#切片的用法
strMsg='hello world!'
# slice[start:end:step]
# 切片的结构其中：
# 1.start<=value<end就是前闭后开区间。
# 2.第一个元素的下标值为0。
# 3.当取到了最开始的元素或者最后的元素的时候不用在[]中填规定数据。
print(strMsg)#输出完整的数据。
print(strMsg[0])#取出第1个数据。
print(strMsg[2:5])#取出第三个到第六个之间的元素，[]为前闭后开区间，第一数据的下标值为0！！！
print(strMsg[2:])#取出第三个到最后一个元素的数据。
print(strMsg[0:3])#1-3
print(strMsg[:3])#运行结果与上一行代码结果一样。所以（给定了是从开始取或者是取到结尾可以把start或者end的值省略！！！）
print(strMsg[::-1])#最后一个步长的正负决定输出结果的方向即正的就是：从左往右正序输出，负的就从右往左倒序输出。
pass
