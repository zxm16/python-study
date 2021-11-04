# # for循环
# # 语法特点遍历操作，依次取集合容器中的每一个值
# # for 临时变量 in 容器：
# #     执行代码块
# tags="我是一个中国人" #字符串类型本沈就是一个字符类型的集合
# for item in tags:
#     print(item)
#     pass
# # range 此函数能生成一个数据集合列表
# # range(起始：结束：步长) 步长不能为0
# sum=0
# for data in range(1,100):#数据是做包含右不包含
#     sum+=data #求和累加
#     print(data,end=" ")
#     print("sum=%d"%sum)
print("--------------------------")
for data in range(1,100):
    if data%2==0:
        print("偶数项有：%d"%data)
    else:
        print("基数项有：%d"%data)
        pass
print("-------------------------")
