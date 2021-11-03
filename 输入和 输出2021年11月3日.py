# 输出
name="张吃饭"
classpro="武昌理工学院"
age=22
print('我的名字是%s,我今年%d岁了：来自【%s】'%(name,age,classpro))
# /n换行效果
print('我可以\n换行吗')

#练习输出
print('------------------------')
name="张吃饭"
QQ=12345678
phone=12345678
Adress='武汉市新洲区1'
print('名字:%s\n QQ:%d\n 手机号：%d\n 公司地址:%s\n'%(name,QQ,phone,Adress))

print('QQ:{}'.format(QQ))
print('手机号：{}'.format(phone))
print('地址：{}'.format(Adress))
print('姓名：{}'.format(name))
# 格式输出的其他方式.format()
print('-------------------------')

#input练习 获取键盘输入内容
#第一种方式
name=input('请输入你的姓名')
QQ=input('请输入你的QQ')
phone=input('请输入你的电话')
Adress=input('请输入你的地址')
Age=input('请输入您的年龄')

print('QQ:{}'.format(QQ))
print('手机号：{}'.format(phone))
print('地址：{}'.format(Adress))
print('姓名：{} 今年：{}了'.format(name,Age))

# 第二种方式
name=input('请输入你的姓名:')
QQ=input('请输入你的QQ:')
phone=input('请输入你的电话:')
Adress=input('请输入你的地址:')
Age=int(input('请输入您的年龄:'))

print('QQ:{}'.format(QQ))
print('手机号：{}'.format(phone))
print('地址：{}'.format(Adress))
print('今年：%d了'%(Age))
print('姓名：{} '.format(name))
