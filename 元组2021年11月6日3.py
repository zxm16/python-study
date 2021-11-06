# 元组的创建,因为不能修改，所以不能增删改查，只能对元组进行查找。
tupleA=()#空元组
print(type(tupleA))
pass
tupleA=('abcd',89,9.13,'joker',3333,[1,2,33])
print(tupleA)
pass


print('-----------------------元组的查询------------------------')
print('-------------通过for来正序遍历----------')
tupleB=('abcd',89,9.13,'joker',333,[1,2,33])
for item in tupleB:
    print(item,end=' ')
    pass
pass

print('---------------元组正序切片取值----------')
tupleC=('abcd',89,9.13,'joker',333,[1,2,33])
print(tupleC[1:3])
pass

print('-------------对元组进行倒序遍历----------')
tupleD=('abcd',89,9.13,'joker',333,[1,2,33])
print(tupleD[::-1])
pass

print('---------------元组倒序切片取值----------')
tupleE=('abcd',89,9.13,'joker',333,[1,2,33])
print(tupleE[-3:-1:1])
#倒序查询就是从右往左进行赋予索引值，但取值范围还是遵循前闭后开原则，
# 所以像现在的例子就是取倒序的第3项和第4项。
# （因为前开后闭那么-3可取，那索引值就是4那么就是元组中倒序的第4个值，
# -1不可取得取它后一项那就是-2，那索引值就是3那么是倒序的第3个值。）
pass

print('--------元组正序更改步长切片取值----------')
tupleF=('abcd',89,9.13,'joker',333,[1,2,33],444,888)
print(tupleF[1:6:2])
print(tupleF[0:7:3])
#1.不管步长为多少第一取值的第一项都得取，然后再从第一项取相应步长的数。
#2.我们可以看到更改步长输出的值都是规定步长取到值得最后一位。
pass

print('--------元组倒序更改步长切片取值----------')
tupleG=('abcd',89,9.13,'joker',333,[1,2,33],444,555,777)
print(tupleG[-6:-1:2])
print(tupleG[-6:-1:3])
tupleG[5][0]=444#可以对元组里的列表进行修改
print(tupleG)
pass


print('---------------当只有一个数不加逗号就不是元组------------------')
print('--------不带逗号----------')
tupleM=(1)
print(type(tupleM))
pass

print('--------带逗号----------')
tupleN=(1,)
print(type(tupleN))
pass

print('---将不是元组类型的转换为元组类型--')
tupleO=tuple(range(10))
print(type(tupleO))
pass


print('---------统计元组中有多少个相同的数据值，注意不是索引值-------------')
tupleP=(1,2,3,4,4,5,5,5,6,6,6,6,6,6)
print(tupleP.count(6))
pass
