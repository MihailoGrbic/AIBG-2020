from Bot import Bot
from BotGoTo import BotGoTo
from utils import *

class BotRushOnePart(Bot):

    def play_single_turn(self, current_game_state):
        x = current_game_state.self_info.x
        y = current_game_state.self_info.y
        if x > 12: target_x = 14
        else:  target_x = 10
        if y > 12: target_y = 14
        else:  target_y = 10

        print(target_x)
        print(target_y)
        
        if len(current_game_state.self_info.player_info['parts']) < 1:
            if "singleDigTarget" not in current_game_state.internal_bot_state:
                diggable_tiles = get_all_non_digged(current_game_state.map, (x, y))
                if len(diggable_tiles) > 0:
                    (dig_x, dig_y) = find_closest_coordinate((x, y), diggable_tiles)
                    current_game_state.internal_bot_state["singleDigTarget"] = (dig_x, dig_y)

            if "singleDigTarget" in current_game_state.internal_bot_state:        
                (dig_x, dig_y) = current_game_state.internal_bot_state["singleDigTarget"]     
                print(dig_x)
                print(dig_y)   
                if dig_x != x or dig_y != y:
                    return move_once(current_game_state, (dig_x, dig_y))
                else:
                    if current_game_state.map.tiles[dig_y][dig_x]['diggingLevel'] != 0:
                        return actions.dig()
                    else:
                        return actions.collect()

        print(target_x)
        print(target_y)
        return move_once(current_game_state, target=(target_x, target_y))
        
        




