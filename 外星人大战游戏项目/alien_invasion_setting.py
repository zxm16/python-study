class Setting:
    """
    储存游戏中所有设置的类
    """
    def __init__(self):
        # 初始化游戏设置
        # 设置屏幕样式
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.5
        # 飞船设置
