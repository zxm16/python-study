import sys

import pygame

from alien_invasion_setting import Setting

from alien_invasion_ship import Ship


class AlienInversion:
    """
        管理游戏资源和行为的类
        """

    def __init__(self):
        """
        初始化游戏，并建立资源
        """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Inversion')
        self.bg_color = (230, 230, 230)
        # 设置背景颜色

        self.settings = Setting()
        # 将Setting实例赋给self.settings来调用Setting
        self.ship = Ship(self)
        # 将Ship实例赋给self.ship来调用Ship

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # 将Setting中初始化的设置通过self.screen来调用

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监视鼠标和鼠标事件
            self._check_event()
            # 循环开始调用_check_event()方法来执行游戏
            self._update_event()
            # 循环开始调用_update_event()方法来更新画面


    def _check_event(self):
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                sys.exit()

    def _update_event(self):
        """ 更新屏幕上的图像并切换到新屏幕"""
        self.screen.fill(self.bg_color)
        # 每次循环时都重绘屏幕，调用fill()方法将本颜色充满屏幕
        self.ship.blitme()
        # 调用blitme将飞船绘制在屏幕上

        pygame.display.flip()
        # 让最近绘制的屏幕可见 (不断更新屏幕)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInversion()
    ai.run_game()



