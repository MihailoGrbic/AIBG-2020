from Bot import Bot
from utils2 import *
from utils import *

class BotCollectSell(Bot):
    def play_single_turn(self, current_game_state: GameState):
        dig_tiles = get_all_non_digged()
        self_info = current_game_state.self_info.player_info
        self_pos = (self_info['x'], self_info['y'])
        if len(dig_tiles) == 0:
            path = astar(current_game_state.map, current_game_state.other_info, (self_info['x'], self_info['y']),
                         (dig_tiles[0][0], dig_tiles[0][1]))
            print(path[0])
        else:
            sol = get_discovery_tiles_per_direction(current_game_state.map, self_pos)
            print (sol)
            return max('w', 's', 'a', 'd', key= lambda dir: sol[dir])
