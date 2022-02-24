import sys
import pygame
from AlienInvasion_setting_12_6 import Settings
from AlienInvasion_ship_12_6 import Ship
from AlienInvasion_bullet_12_6 import Bullet


class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.bg_color = (135, 206, 235)
        # 设置背景颜色
        self.screen = pygame.display.set_mode((1200, 800))
        #  self.screen  ←  设置窗口尺寸

        self.settings = Settings()

        self.ship = Ship(self)

        pygame.display.set_caption('意大利炮大战马保国')
        # 设置窗口标题

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        
        self.bullets = pygame.sprite.Group()

    def run(self):
        while True:
            self._update_screen()
            self.ship.update()
            self._check_event()
            self._update_bullet()

            for bullet in self.bullets.copy():

                if bullet.rect.bottom < 0:

                    self.bullets.remove(bullet)

            print(len(self.bullets))

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                sys.exit()

            elif event.type == pygame.KEYDOWN:

               self._check_events_keydown(event)

            elif event.type == pygame.KEYUP:

                self._check_events_keyup(event)

    def _check_events_keydown(self, event):

        if event.key == pygame.K_RIGHT:

            self.ship.move_right = True

        elif event.key == pygame.K_LEFT:

            self.ship.move_left = True

        elif event.key == pygame.K_SPACE:

            self._fire_bullet()

    def _check_events_keyup(self, event):

        if event.key == pygame.K_RIGHT:

            self.ship.move_right = False

        elif event.key == pygame.K_LEFT:

            self.ship.move_left = False

    def _update_screen(self):

        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.bullets.sprites():

            bullet.draw_bullet()

        pygame.display.flip()

    def _fire_bullet(self):

        if len(self.bullets) < self.settings.bullet_allowed:

            new_bullet = Bullet(self)

            self.bullets.add(new_bullet)

    def _update_bullet(self):

        self.bullets.update()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run()




