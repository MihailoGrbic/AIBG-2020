from Bot import Bot
from BotGoTo import BotGoTo
from utils import *

class BotGuardShop(Bot):

    def play_single_turn(self, current_game_state):
        x = current_game_state.self_info.x
        y = current_game_state.self_info.y
        print(current_game_state.self_info.player_info)
        
        return 'a'
