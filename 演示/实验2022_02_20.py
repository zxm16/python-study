import copy

spam = [1, 2, 3, 4, 5]
print(id(spam))
English = copy.deepcopy(spam)
English.insert(0, 3)
print(English)
print(spam)
print(id(English))
chinese = copy.copy(spam)
print(chinese)
print(id(chinese))

z = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = 0
while y < 3:
    for x in range(0, 3):
        print(z[x][y], end=' ')
    y += 1
    print('\n')
