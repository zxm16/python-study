# 循环的分类
# while 语法结构
# while 条件表达式：
#     代码指令

# 语法特点：
# 1.有初始值
# 2.有条件表达式
# 3.循环数变量【循环体内的计数变量】必须是自增或自减，否者会造成死循环
# 4.使用条件：循环的次数不确定，是依靠循环条件来结束
# 目的：为了将相似或相同的代码操作变得更加简洁，使得代码可以重复利用

# for

# while的使用案例：
# 1.输出1-100之间的数据
i=1
# 定义一个变量
while i<=100:
    print(i)
    i+=1

    pass

# 2.猜拳击的小游戏
# 0：石头 1：剪刀:2：布
import random#调用计算机的随机数指令
# 计算机 人
i=1
while i<=10:
    person=int(input("请出拳：[0：石头 1：剪刀:2：布]"))
    computer=random.randint(0,2)#设置随机指令的取值范围
    if person==0 and computer==2:
        print('你输了')
    elif person==0 and computer==1:
        print('你赢了')
    elif person==1 and computer==0:
        print('你输了')
    elif person==1 and computer==2:
        print('你赢了')
    elif person==2 and computer==0:
        print('你赢了')
    elif person==2 and computer==1:
        print('你输了')
    elif person==computer:
        print('打成平手')
        pass
    i+=1

# 3.打印99乘法表
row=9
while row>=1:
    col=1
    while col<=row:
        print("%d*%d=%d"%(col,row,col*row),end=" ")
        col+=1
        pass
    print()
    row-=1
    pass

# 4.打印直角三角形
row=1
while row<=30:
    col=1
    while row>=col:
        print("*",end="")
        col+=1
        pass
    print()
    row+=1
    pass

# 方向相反的支教三角形
row=30
while row>=1:
    col=1
    while row>=col:
        print("*",end="")
        col+=1
        pass
    print()
    row-=1
    pass

# 练习打印等腰三角形
row=1
while row<=5:
    j=1
    while j<=10-row:
        print(" ",end="")
        j+=1
        pass
    k=1
    while k<=2*row-1:
        print("*",end="")
        k+=1
        pass
    print()
    row+=1
