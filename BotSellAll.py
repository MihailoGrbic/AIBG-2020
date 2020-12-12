from Bot import Bot
from BotGoTo import BotGoTo
from utils import *

class BotSellAll(Bot):

    def play_single_turn(self, current_game_state):
        min_path = 100
        target_x = 10
        target_y = 10
        for tile in shopping_tiles:
            path = find_path_to(current_game_state.self_info, current_game_state.other_info, current_game_state.map, tile[0], tile[1])
            if min_path > len(path):
                min_path = len(path)
                target_x = tile[0]
                target_y = tile[1]
        
        if current_game_state.self_info.x == target_x and current_game_state.self_info.y == target_y:
            for part in current_game_state.self_info.player_info['parts']:
                return actions.sell_part(part["id"])

        return move_once(current_game_state, target=(target_x, target_y))
        
        




