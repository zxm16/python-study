import pygame


class Ship:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        # 将屏幕赋值给self.screen

        self.setting = ai_game.settings
        # 添加一个设置链接设置模块来控制飞船移动距离

        self.screen_rect = ai_game.screen.get_rect()
        # 访问屏幕的rect并且其值赋给self.screen_rect

        # self.screen_rect = ai_game.screen.get_rect
        # 没有的括号导致方法没有调用后面报错

        self.image = pygame.image.load('ship.png')
        # 加载飞船
        self.rect = self.image.get_rect()
        # 设置加载飞船的外接矩形

        self.rect.midbottom = self.screen_rect.midbottom
        # 让每艘新飞船都在屏幕中央

        self.x = float(self.rect.x)
        # 在飞船x中储蓄最小值

        self.moving_right = False
        # 向右移动标志

        self.moving_left = False
        # 向左移动标志

    def update(self):
        """
        向左向右移动飞船并且设置其速度
        及固定左右边使其到边停止
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 当移动数值小于屏幕的长度时可以一直移动。

            self.x += self.setting.ship_speed
            # 在基础移动距离的情况下一直增加（累加）ship_speed这样速度会越来越快

        if self.moving_left and self.rect.left > 0:
            # 当x值大于0时可以一直向左运动

            self.x -= self.setting.ship_speed
            # 在基础移动距离的情况下一直减少（递减）ship_speed这样速度会先减少再一直往反方向增加

        self.rect.x = self.x
        # 更新飞船在x轴的位置

    def blitme(self):
        """
        在指定位置绘制飞船
        """
        self.screen.blit(self.image, self.rect)
