# break和continue
# sum=0
for item in range(1,51):
    if sum>100:
        print("循环到这个数就不再循环了：%d"%item)
        break#退出循环体
    pass
    sum+=item
    pass
    print("sum=%d"%sum)

print("---------conntinue展示-------------")
for item in range(1,100):#求出来偶数
    if item%2==0:
        continue
        print("在continue后会不会运行呢？")
        pass
    print(item)
    pass

print("-------continue展示--------------")
for item in 'i like study than you!':
    if item=='e':
        break#break是彻底中断
    print(item,end=' ')
    pass


print("-------continue展示--------------")
for item in 'i like study than you!':
    if item=='s':
        continue#continue是跳过后面继续继承
    print(item,end=' ')
    pass



index=1
while index<=100:
    if index>20:
        break
        pass
    print(index,end=' ')
    index+=1




# 99乘法表用for来实现
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j),end=' ')
        pass
    print()#控制换行
    pass


for i in range(1,100):
    print(i,end=' ')
    if i>=5:
        break
        pass
    else :
        print('还在执行')


account='zcf'
password='123'
for i in range(3):
    zh=input('请输入账号：')
    pd=input('请输入密码：')
    if account==zh and password==pd:
        print('登录成功')
        continue
        pass
    else:
        print('登录失败请重新输入密码')
    pass
else:
    print('您的账号已经锁定')
