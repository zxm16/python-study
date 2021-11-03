# 逻辑运算符 and or not
# and 比较严格 两边结果必须都为true则输出结果为true
a,b,c,d=23,18,10,3
print(a+b>c and c<d)
print(c>d and a>d)

# 条件有一个真即为真
print(a<b or b>d)
print(a>b or b<d)

# not 取反 真假互换
print(not a>b)
print(not a<b)

# 优先级
# ()->not->and->or
print(2>1 and 1<4 or 2<3 and 9>6 or 2<4 and 3<2)

# 赋值运算
# =，+=，-=，%=，*=，/=,**=,//=
a,b,c,d=23,18,10,3
a+=c
a**=c
print(a)
