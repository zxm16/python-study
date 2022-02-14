# 9.13 骰子
print('-----------9-13-----------')


class Die:

    def __init__(self, sides=6):
        self.sides = sides
        # 定义一个初始化属性sides来表示骰子的的面数

    def roll_die(self):
        from random import randint
        self.sides = randint(1, 6)
        print(self.sides)
        # 运用标准库随机生成一个面


Die01 = Die()
# 将Die类赋值个给Die01
Die01.roll_die()
# 打印10次模仿丢了10次骰子
Die01.roll_die()
Die01.roll_die()
Die01.roll_die()
Die01.roll_die()
Die01.roll_die()
Die01.roll_die()
Die01.roll_die()
Die01.roll_die()
Die01.roll_die()
print('-----------------下一题------------------------')


# 9.14彩票
print('-----------9-14-----------')
print('当抽到数字10的时候才能中奖')


class Money:

    def __init__(self, money01=1):
        self.money01 = money01

    def money(self):
        from random import choice
        number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.money01 = choice(number)
        print(f'你抽中的幸运数字是:{self.money01}')
        if self.money01 == 10:
            print('恭喜你中奖了！')
        else:
            print('很遗憾，下次再接再厉！')


ticket = Money()
ticket.money()
print('-----------------下一题------------------------')


# 9.15彩票分析
print('-----------9-15-----------')
print('当抽到数字10的时候才能中奖')


class Money:

    def __init__(self, money01=1):
        self.money01 = money01

    def money(self):
        while True:
            from random import choice
            number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
            self.money01 = choice(number)
            print(f'你抽中的幸运数字是:{self.money01}')
            if self.money01 == 10:
                print('恭喜你中奖了！')
                break
            else:
                print('很遗憾，下次再接再厉！')


ticket = Money()
ticket.money()
print('-----------------下一题------------------------')
