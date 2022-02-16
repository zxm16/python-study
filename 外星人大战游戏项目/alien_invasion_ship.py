import pygame


class Ship:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        # 将屏幕赋值给self.screen
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

    def blitme(self):
        """
        在指定位置绘制飞船
        """
        self.screen.blit(self.image, self.rect)
