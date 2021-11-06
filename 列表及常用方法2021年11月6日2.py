li=[1,2,3,"你好"]
print(len(li))#len可以获取列表对象中的数据个数，也可以用在字符串中。
print(type(li))
pass


#列表中的切片操作和方法
print("----------------------------增------------------------------")

print("------------原始插入----------------")
#增加
#append的使用
#append插入的数据只能加到列表的最后面
listB=['ABCD',2222,3.33,True,"求知"]
print("追加之前：",listB)
listB.append(["yyds",222,22,3,"a"])#append的结构是append()
listB.append(233)#如果加入元素过多要么将元素定义为一个列表加入如：.append(["yyds",222,22,3,"a"])，要么就一个一个加不然会报错
print("追加之后：",listB)
print(listB)
pass

print("-----------指定位置插入-------------")

#insert的使用
#insert可以指定所插入元素插入的位置
listC=['ABCD',2222,3.33,True,"求知"]
listC.insert(1,"这是刚插入的数据")#解释:(指定的位置即0-~~，插入的对象)
print(listC)
pass

print("------------大量插入----------------")
#extend批量添加元素得列表输入后面
listD=['ABCD',2222,3.33,True,"求知"]
rsDate=list(range(10))#将range随机生成的数强制转换为list对象
listD.extend(rsDate)
# '''extend是继承的意思就是listD继承rsDate里的列表数据，
# 同样也只能加一个元素，但是加入的列表不是表中表，
# 而是将列表的元素添加到父列表中。'''
print(listD)
pass



print("----------------------------删------------------------------")

print("-----------del指定位置删除-------------")
listF=['ABCD',2222,3.33,True,"求知"]
print('删除之前：',listF)
del listF[0]
print('删除之后：',listF)
pass

print("-------------del批量删除---------------")
listG=['ABCD',2222,3.33,True,"求知"]
print('删除之前：',listG)
del listG[1:3]
print('删除之后：',listG)
pass

print("-------------remove删除---------------")
listH=list(range(1,50))
print('删除之前：',listH)
listH.remove(20)#移除给定项的数据值
print('删除之后：',listH)
pass

print("----------------pop删除---------------")
listI=list(range(1,50))
print('删除之前：',listI)
listI.pop(20)#移除给定项的索引值
print('删除之后：',listI)
pass



print("----------------------------改------------------------------")

print("-----------修改它的值-------------")
listE=['ABCD',2222,3.33,True,"求知"]
print('修改之前：',listE)
listE[4]='b站'#以知那个元素在列表的位置可以直接修改
print('修改之后：',listE)
pass



print("------------------------查---------------------------------")

print("----------------index查找---------------")
listA=['ABCD',2222,3.33,True,"b站"]
print(listA)#输出完整的list
print(listA[0])#输出第一个元素
print(listA[1:3])#输出第二个到第三个元素
print(listA[2:])#输出第三个元素开始到最后一个元素
print(listA[::-1])#输出倒序的list
print(listA*2)#输出多次list的数据（相当于复制几次）
pass

print("----------------index查找---------------")
listJ=list(range(1,50))
print(listJ.index(1))#打印元素所在的索引值
print(listJ.index(1,2,25))#意思就是：（查找1这个值,从第二项开始查起，往后查25项）
# 因为“1”这个值是索引地址是0，但他是从第3项开始查起，而且后面25项也不包含1，所以输出的是“1”这个不在列表之中。
pass
