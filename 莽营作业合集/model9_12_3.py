from model9_12_2 import AdminPower

AdminPower01 = AdminPower('张', '鑫满')
AdminPower01.print_hello_admin()
# 调用打印管理员名字的方法
print('---小题分界线---')
AdminPower01.adminer.admin_name('你可以添加这个')
# 执行admin_name方法，向列表添加元素
AdminPower01.adminer.admin_name01()
# 执行admin_name01方法，打印这个列表
AdminPower01.adminer.admin_name('你可以删除这个')
# 执行admin_name方法，向列表添加元素
AdminPower01.adminer.admin_name01()
AdminPower01.adminer.admin_name('你可以移动那个')
AdminPower01.adminer.admin_name01()
AdminPower01.adminer.admin_name03()
# 执行admin_name03将列表里每一个元素进行与字符串结合打印出来
