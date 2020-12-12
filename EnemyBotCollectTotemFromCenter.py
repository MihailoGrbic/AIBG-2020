from BotStateMachine import BotStateMachine
from utils import *
import actions
from GameState import GameState

class EnemyBotCollectTotemFromCenter(BotStateMachine):

    def get_action_and_state(self, current_game_state: GameState, bot_state):

        self_info = current_game_state.self_info
        curr_tile = current_game_state.map.tiles[self_info.y][self_info.x]

        if bot_state == 'initial':
            goal = (9, 9)

            if goal[0] == self_info.x and goal[1] == self_info.y:
                return 'first_dig', actions.down()

            return 'initial', get_next_action_towards(current_game_state.map, current_game_state.other_info,
                                                        (self_info.x, self_info.y),
                                                        goal)

        elif bot_state == 'first_dig':

            if curr_tile['tileType'] == "DIGTILE":
                if curr_tile["dug"] == False:
                    return 'first_dig', actions.dig()
                if curr_tile['part'] is not None:
                    current_game_state.internal_bot_state['other_tile_pos'] = get_symetric_pos(current_game_state.map, self_info.pos)
                    if curr_tile['part']['totemType'] != "NEUTRAL":
                        if len(self_info.player_info['parts']) == 3:
                            neutral_part_id = None
                            for part in self_info.player_info['parts']:
                                if part['totemType'] == "NEUTRAL":
                                    neutral_part_id = part['id']
                            return 'other_part', actions.swap_part(neutral_part_id)
                        else:
                            return 'other_part', actions.collect()
                    if curr_tile['part']['totemType'] == "NEUTRAL" and len(self_info.player_info['parts']) < 3:
                        return 'first_dig', actions.collect()

            dig_tiles = get_all_non_digged(current_game_state.map, (self_info.x, self_info.y))

            if len(dig_tiles) != 0 and dig_tiles[0][0] == self_info.x and dig_tiles[0][1] == self_info.y:
                del dig_tiles[0]

            if len(dig_tiles) != 0:
                return 'first_dig', get_next_action_towards(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                             (dig_tiles[0][0], dig_tiles[0][1]))
            else:
                return 'first_dig', explore(current_game_state, self_info)

        elif bot_state == 'other_part':
            pos_to_go = current_game_state.internal_bot_state['other_tile_pos']

            if pos_to_go[0] == self_info.pos[0] and pos_to_go[1] == self_info.pos[1]:
                if curr_tile["dug"] == False:
                    return 'other_part', actions.dig()
                elif curr_tile['part'] is not None:
                        if len(self_info.player_info['parts']) == 3:
                            neutral_part_id = None
                            for part in self_info.player_info['parts']:
                                if part['totemType'] == "NEUTRAL":
                                    neutral_part_id = part['id']
                            return 'find_neutral', actions.swap_part(neutral_part_id)
                        else:
                            return 'find_neutral', actions.collect()
                else:
                    #abandon, just sell it all
                    return 'sell', actions.down()

            return 'other_part', get_next_action_towards(current_game_state.map, current_game_state.other_info,
                                                      (self_info.x, self_info.y),
                                                      pos_to_go)

        elif bot_state == 'find_neutral':
            if len(self_info.player_info['parts']) == 3:
                return 'sell', actions.down()

            if curr_tile['tileType'] == "DIGTILE":
                if curr_tile["dug"] == False:
                    return 'find_neutral', actions.dig()
                if curr_tile['part'] is not None:
                    if curr_tile['part']['totemType'] == "NEUTRAL":
                        return 'sell', actions.collect()

            dig_tiles = get_all_non_digged(current_game_state.map, (self_info.x, self_info.y))

            if len(dig_tiles) != 0 and dig_tiles[0][0] == self_info.x and dig_tiles[0][1] == self_info.y:
                del dig_tiles[0]

            if len(dig_tiles) != 0:
                return 'find_neutral', get_next_action_towards(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                             (dig_tiles[0][0], dig_tiles[0][1]))
            else:
                return 'find_neutral', explore(current_game_state, self_info)

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
                totems = {}
                for part in self_info.player_info['parts']:
                    if part['totemType'] not in totems:
                        totems[part['totemType']] = 0
                    totems[part['totemType']] += 1
                for totem in totems:
                    if totems[totem] == 2:
                        return 'initial', actions.sell_totem()

                if len(self_info.player_info['parts']) == 1:
                    return 'initial', actions.sell_part(self_info.player_info['parts'][0]['id'])
                else:
                    return 'sell', actions.sell_part(self_info.player_info['parts'][0]['id'])


            return 'sell', get_next_action_towards(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                         (loc_to_go[0], loc_to_go[1]))

