import sys

import pygame

from alien_invasion_setting import Setting

from alien_invasion_ship import Ship

from alien_invasion_bullet import Bullet


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
        
        # self.screen = pygame.display.set_mode((0, 0,), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.ship = Ship(self)
        # 将Ship实例赋给self.ship来调用Ship

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # 将Setting中初始化的设置通过self.screen来调用
        self.bullet = pygame.sprite.Group()

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监视鼠标和鼠标事件
            self._check_event()
            # 循环开始调用_check_event()方法来执行游戏

            self._update_event()
            # 循环开始调用_update_event()方法来更新画面

            self.ship.update()
            # 运行飞船模块
            self._update_bullet()
            # 调用更新子弹的位置
            
            for bullets in self.bullet.copy():
                # 因为不能直接从bullet中删除子弹
                # 所以遍历整个bullet将其超过边界的bullet移除
                if bullets.rect.bottom <= 0:
                    # 判断当子弹的边界小于0即超过边界时的操作
                    self.bullet.remove(bullets)
                    # 将超过边界的子弹从bullet中移除
                print(len(self.bullet))
                # 打印子弹还有多少

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 如果事件为在pygame中按x键：
                sys.exit()
                # 系统退出

            elif event.type == pygame.KEYDOWN:
                # 如果事件为在pygame中按下按键时：
                self._check_keydown_events(event)
                # 按下指定按键使飞船一直向上下左右移动

            elif event.type == pygame.KEYUP:
                # 如果事件为在pygame中按下按键时：
                self._check_keyup_events(event)
                # 松开指定按键使飞船一直向上下左右移动

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # 如果按下的是键盘右键时：

            self.ship.moving_right = True
            # 向右移动启动（即一直按下按键就会一直运动）

        elif event.key == pygame.K_LEFT:
            # 如果按下的是键盘左键时：

            self.ship.moving_left = True
            # 向左移动启动（即一直按下按键就会一直运动）

        elif event.key == pygame.K_q:
            # 如果按下的是q键的话程序退出
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            # 如果按下的是键盘右键时：

            self.ship.moving_right = False
            # 向右移动关闭（即松开按键就会停止运动）

        elif event.key == pygame.K_LEFT:
            # 如果按下的是键盘左键时：

            self.ship.moving_left = False
            # 向左移动关闭（即松开按键就会停止运动）

    def _fire_bullet(self):
        if len(self.bullet) < (self.settings.bullets_allowed):
            # 当子弹小于3颗的时候创造一颗子弹
            new_bullet = Bullet(self)
            # 赋值来通过new_bullet来调用Bullet类

            self.bullet.add(new_bullet)
            # 将Bullet类添加到实例中

    def _update_event(self):
        """ 更新屏幕上的图像并切换到新屏幕"""
        self.screen.fill(self.bg_color)
        # 每次循环时都重绘屏幕，调用fill()方法将本颜色充满屏幕

        self.ship.blitme()
        # 调用blitme将飞船绘制在屏幕上

        for bullet in self.bullet.sprites():
            # 使用循环来一直调用子弹
            bullet.draw_bullet()

        print(len(self.bullet))

        pygame.display.flip()
        # 让最近绘制的屏幕可见 (不断更新屏幕)

    def _update_bullet(self):
        """
        更新子弹的位置并删除子弹
        :return:
        """
        self.bullet.update()
        # 运行子弹模块


if __name__ == '__main__':
    # 创建游戏实例并运行游戏

    ai = AlienInversion()
    ai.run_game()



