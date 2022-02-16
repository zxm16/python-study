import sys
import pygame


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        #  self.screen  ←  设置窗口尺寸
        pygame.display.set_caption('意大利炮大战马保国')
        # 设置窗口标题
        self.bg_color = (135, 206, 235)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run()
