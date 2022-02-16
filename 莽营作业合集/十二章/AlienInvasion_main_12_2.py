import sys
import pygame
from AlienInvasion_setting_12_2 import Settings
from AlienInvasion_ship_12_2 import Ship


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.bg_color = (135, 206, 235)
        self.screen = pygame.display.set_mode((1200, 800))

        self.setting = Settings()
        self.ship = Ship(self)
        pygame.display.set_caption('意大利炮大战马保国')
        # 设置窗口标题

        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height)
        )
        #  self.screen  ←  设置窗口尺寸

    def run(self):
        while True:
            self._check_event()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run()




