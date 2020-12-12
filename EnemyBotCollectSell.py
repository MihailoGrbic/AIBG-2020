from Bot import Bot
from GameState import GameState
from utils import *
import actions

class EnemyBotCollectSell(Bot):

    def play_single_turn(self, current_game_state: GameState):

        self_info = current_game_state.self_info

        curr_tile = current_game_state.map.tiles[self_info.y][self_info.x]

        bazar_locs = [
            (10, 10),
            (14, 14),
            (10, 14),
            (14, 10)
        ]

        loc_to_go = min(bazar_locs, key=lambda loc: dist(loc, self_info.pos))

        if dist(loc_to_go, self_info.pos) == 0 and len(self_info.player_info['parts']) > 0:
        # we're at bazar! sell
            return actions.sell_part(self_info.player_info['parts'][0]['id'])

        if len(self_info.player_info['parts']) == 3:
            # go to bazar

            return get_next_action_towards(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                         (loc_to_go[0], loc_to_go[1]))

        if curr_tile['tileType'] == "DIGTILE":
            if curr_tile["dug"] == False:
                return actions.dig()
            if curr_tile['part'] is not None:
                return actions.collect()

        dig_tiles = get_all_non_digged(current_game_state.map, (self_info.x, self_info.y))

        if len(dig_tiles) != 0 and dig_tiles[0][0] == self_info.x and dig_tiles[0][1] == self_info.y:
            del dig_tiles[0]

        if len(dig_tiles) != 0:
            return get_next_action_towards(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                         (dig_tiles[0][0], dig_tiles[0][1]))
        else:
            sol = get_discovery_tiles_per_direction(current_game_state.map, self_info)
            print (sol)
            allactions = [actions.up(), actions.down(), actions.left(), actions.right()]
            max_ = max([sol[action] for action in allactions])
            only_max_actions = [action for action in allactions if sol[action] == max_]
            return random.choice(only_max_actions)
