from Bot import Bot
from utils import *

class BotRushOnePart(Bot):

    def __init__(self):
        start_x = current_game_state.self_info.x
        start_y = current_game_state.self_info.y
        if start_x > 12: self.target_x = 13
        else:  self.target_x = 11
        if start_y > 12: self.target_y = 13
        else:  self.target_y = 11

    def play_single_turn(self, current_game_state):
        print(current_game_state.turns_left)
        for tile in current_game_state.map.tiles:
            if tile['tileType'] == 'DIGTILE':
                print("vuhu")
        return move_once(current_game_state, target=(self.target_x, self.target_y))
        
        




