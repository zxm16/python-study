import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.color = self.setting.bullet_color

        self.rect = pygame.Rect(0, 0, self.setting.bullet_width,
                                self.setting.bullet_height)
        # 创建矩形（子弹不是图像画出的所以要用pygame.rect()调用）

        self.rect.midtop= ai_game.ship.rect.midtop
        # 设置子弹从飞船顶部出发

        self.y = float(self.rect.y)
        # 储存小数表示子弹位置

    def update(self):
        """ 向上移动子弹"""
        self.y -= self.setting.ship_speed
        # 发射出去后子弹y的坐标不断减小

        self.rect.y = self.y
        # 更新子弹的位置

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

