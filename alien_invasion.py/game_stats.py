class GameStats():
    """跟踪游戏的统计信息"""



    def __init__(self, ai_settings):
        last_high_score = 0
        
        with open('highscore.txt') as file_object:
            last_high_score = int(file_object.read())
        
        """初始化统计"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #游戏刚启动时处于活动状态
        self.game_active = False
        #记录最高得分，不重置
        self.high_score = last_high_score
        self.last_high_score = last_high_score

    def reset_stats(self):
        """初始化可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        

