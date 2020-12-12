from Bot import Bot
from utils import *

class BotBodyBlock(Bot):

    def __init__(self, blocked_tiles, expected_jukes = "safe"):
        self.counter = 0
        self.blocked_tiles = blocked_tiles
        self.expected_jukes = expected_jukes

    def play_single_turn(self, current_game_state):
        if current_game_state.opponent_visible:
            enemy_x = current_game_state.other_info.player_info["x"]
            enemy_y = current_game_state.other_info.player_info["y"]
            self_x = current_game_state.self_info.player_info["x"]
            self_y = current_game_state.self_info.player_info["y"]
        
        left_target = [enemy_y, enemy_x - 1, 0]
        right_target = [enemy_y, enemy_x + 1, 0]
        above_target = [enemy_y - 1, enemy_x, 0]
        bellow_target = [enemy_y + 1, enemy_x, 0]

        while not move_available(current_game_state.map, current_game_state.other_info, (left_target[1], left_target[0])):
            left_target[1] -= 1
        while not move_available(current_game_state.map, current_game_state.other_info, (right_target[1], right_target[0])):
            right_target[1] += 1
        while not move_available(current_game_state.map, current_game_state.other_info, (above_target[1], above_target[0])):
            above_target[0] -= 1
        while not move_available(current_game_state.map, current_game_state.other_info, (bellow_target[1], bellow_target[0])):
            bellow_target[0] += 1          

        for tile in self.blocked_tiles:
            if tile[1] <= left_target[1]: left_target[2] +=1
            if tile[1] >= right_target[1]: right_target[2] +=1
            if tile[0] <= above_target[0]: above_target[2] +=1
            if tile[0] >= bellow_target[0]: bellow_target[2] +=1

        final_target = left_target
        for target in [right_target, above_target, bellow_target]:
            if final_target[2] < target[2]:
                final_target = target
    
        final_target = (final_target[1], final_target[0])
        print(final_target)
        return move_once(current_game_state, final_target)




