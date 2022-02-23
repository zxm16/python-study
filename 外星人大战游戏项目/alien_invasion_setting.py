class Setting:
    """
    储存游戏中所有设置的类
    """
    def __init__(self):
        # 初始化游戏设置
        # 设置屏幕样式
        self.screen_width = 1200
        # 设置屏幕的宽度

        self.screen_height = 800
        # 设置屏幕的高度

        self.bg_color = (230, 230, 230)
        # 设置屏幕的背景颜色

        self.ship_speed = 1.5
        # 飞船设置

        self.bullet_speed = 1.0
        # 设置子弹的速度

        self.bullet_width = 3
        # 设置子弹的宽度

        self.bullet_height = 15
        # 设置子弹的高度

        self.bullet_color = (60, 60, 60)
        # 设置子弹的底色

        self.bullets_allowed = 3
        # 设置在场上的子弹只有3颗
