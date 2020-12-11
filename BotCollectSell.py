from Bot import Bot
from GameState import GameState
from utils2 import *
from utils import *
import actions

class BotCollectSell(Bot):
    def play_single_turn(self, current_game_state: GameState):
        
        self_info = current_game_state.self_info
        self_pos = (self_info.x, self_info.y)

        curr_tile = current_game_state.map.tiles[self_pos[0]][self_pos[1]]

        if curr_tile['tileType'] == "DIGTILE" and curr_tile["dug"] == False:
            return actions.dig()

        dig_tiles = get_all_non_digged(current_game_state.map, self_pos)

        if len(dig_tiles) != 0:
            path = astar(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                         (dig_tiles[0][0], dig_tiles[0][1]))
            print(path[0])
            x_diff = path[1][0] - self_info.x
            y_diff = path[1][1] - self_info.y
            if x_diff == 1:
                return actions.right()
            if x_diff == -1:
                return actions.left()
            if y_diff == 1:
                return actions.down()
            return actions.up()
        else:
            sol = get_discovery_tiles_per_direction(current_game_state.map, self_pos)
            print (sol)
            return max('w', 's', 'a', 'd', key= lambda dir: sol[dir])
