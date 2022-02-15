# 10.8 狗和猫

print('----------------10.8---------------')

cat = 'zzzz.txt'
try:
    with open('zzzz.txt') as zz:
        zzz = zz.readlines()
        print(zzz)
except FileNotFoundError:
    print('找不到相关文件')

print('------小题标志--------')

dog_file = 'dog.txt'
with open('dog.txt') as dog_size02:

    try:
        dog_size03 = dog_size02.readlines()
        print(dog_size03)
    except FileNotFoundError:
        print('找不到相关文件')


print('----------------下一题---------------')


# 10.9 静默狗和猫

print('----------------10.9---------------')


try:
     with open('zzzz.txt') as zz:
        zzz = zz.readlines()
        print(zzz)
except FileNotFoundError:
    pass


print('------小题标志--------')


dog_file = 'dog.txt'
with open('dog.txt') as dog_size02:

    try:
        dog_size03 = dog_size02.readlines()
        print(dog_size03)
    except FileNotFoundError:
        print('找不到相关文件')


print('----------------下一题---------------')


