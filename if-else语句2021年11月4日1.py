# if-else语句的嵌套
# 一个场景需要分阶段或层次，做出不同处理
# 要执行内部条件一定要满足外部条件
xuefen=int (input('请输入你的学分：'))
if xuefen>10:
    grade=int(input('请输入你的成绩：'))
    if grade>=80:
        print('恭喜你可以跳级了！')
        pass
    else:
        print('很遗憾你的成绩不达标！')
        pass
    pass
else:
    print('你再不努力可能会留级！')
