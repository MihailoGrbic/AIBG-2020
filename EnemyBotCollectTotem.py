from BotStateMachine import BotStateMachine
from utils import *
import actions

class EnemyBotCollectTotem(BotStateMachine):

    def get_action_and_state(self, current_game_state: GameState, bot_state):

        self_info = current_game_state.self_info
        curr_tile = current_game_state.map.tiles[self_info.y][self_info.x]

        if bot_state == 'initial':

            if curr_tile['tileType'] == "DIGTILE":
                if curr_tile["dug"] == False:
                    return 'initial', actions.dig()
                if curr_tile['part'] is not None:
                    current_game_state.internal_bot_state['other_tile_pos'] = get_symetric_pos(self_info.pos)
                    if curr_tile['part']['totemType'] != "NEUTRAL":
                        return 'other_part', actions.collect()

            dig_tiles = get_all_non_digged(current_game_state.map, self_info)

            if len(dig_tiles) != 0:
                return 'initial', get_next_action_towards(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                             (dig_tiles[0][0], dig_tiles[0][1]))
            else:
                sol = get_discovery_tiles_per_direction(current_game_state.map, self_info)
                print(sol)
                allactions = [actions.up(), actions.down(), actions.left(), actions.right()]
                max_ = max([sol[action] for action in allactions])
                only_max_actions = [action for action in allactions if sol[action] == max_]
                return 'initial', random.choice(only_max_actions)

        elif bot_state == 'other_part':
            pos_to_go = current_game_state.internal_bot_state['other_tile_pos']

            if pos_to_go[0] == self_info.pos[0] and pos_to_go[1] == self_info.pos[1]:
                if curr_tile["dug"] == False:
                    return 'other_part', actions.dig()
                if curr_tile['part'] is not None:
                    return 'find_neutral', actions.collect()

            return 'other_part', get_next_action_towards(current_game_state.map, current_game_state.other_info,
                                                      (self_info.x, self_info.y),
                                                      pos_to_go)

        elif bot_state == 'find_neutral':
            if curr_tile['tileType'] == "DIGTILE":
                if curr_tile["dug"] == False:
                    return 'find_neutral', actions.dig()
                if curr_tile['part'] is not None:
                    if curr_tile['part']['totemType'] == "NEUTRAL":
                        return 'sell', actions.collect()

            dig_tiles = get_all_non_digged(current_game_state.map, self_info)

            if len(dig_tiles) != 0:
                return 'find_neutral', get_next_action_towards(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                             (dig_tiles[0][0], dig_tiles[0][1]))
            else:
                sol = get_discovery_tiles_per_direction(current_game_state.map, self_info)
                print(sol)
                allactions = [actions.up(), actions.down(), actions.left(), actions.right()]
                max_ = max([sol[action] for action in allactions])
                only_max_actions = [action for action in allactions if sol[action] == max_]
                return 'find_neutral', random.choice(only_max_actions)

        elif bot_state == 'sell':
            bazar_locs = [
                (10, 10),
                (14, 14),
                (10, 14),
                (14, 10)
            ]

            loc_to_go = min(bazar_locs, key=lambda loc: dist(loc, self_info.pos))

            if dist(loc_to_go, self_info.pos) == 0 and len(self_info.player_info['parts']) > 0:
                # we're at bazar! sell
                return 'initial', actions.sell_totem()

            return 'sell', get_next_action_towards(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                         (loc_to_go[0], loc_to_go[1]))

