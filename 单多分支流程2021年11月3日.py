# 单分支
# if 条件表达式：比较/逻辑运算符 符合条件的表达式
#     代码指令
#     ~~~~~~

score=40
if score>=60:#满足条件就会输出打印提升
    print('你的成绩合格!加油')
    pass#空语句

print('语句运行结束')



# 双分支
# if  条件表达式：比较 / 逻辑运算符 符合条件的表达式
#     代码指令
#     ~~~~~~
# else:
#     代码指令

score=40 #False
if score>=60:#满足条件就会输出打印提升
    print('你的成绩合格!加油')
    pass
else:
    print('你的成绩不和格！加把劲')
    pass#空语句

print('语句运行结束')


# 多分支的选择【多个条件的选择视情况而定】
# if  条件表达式：比较 / 逻辑运算符 符合条件的表达式
#     代码指令
#     ~~~~~~
# elif 条件表达式：比较 / 逻辑运算符 符合条件的表达式
#     代码指令
#     ~~~~~~
# elif 条件表达式：比较 / 逻辑运算符 符合条件的表达式
#     代码指令
#     ~~~~~~
# else:  //else可以没有
#     代码指令
# 1.特征：只要满足其中一个分支，就会推出本层if语句结构【必定会执行其中一个分支}
# 2.至少有两种情况可以选择
# 3.elif后面必须写上条件和语句
# 4.else是选配得根据实际情况来填写

score=int(input('请输入你的成绩')) #False
if score>80:
    print('你的成绩合格并且分数很高')
    pass
elif score>=60 or score<=80:
    print('你的成绩和格！但还需努力')
    pass  # 空语句
else:
    print('你的成绩不和格！加把劲')
    pass#空语句

print('语句运行结束')




# 多分支 多条件演练
# 猜拳击的小游戏
# 0：石头 1：剪刀:2：布
import random#调用计算机的随机数指令
# 计算机 人
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

print('语句运行结束')
