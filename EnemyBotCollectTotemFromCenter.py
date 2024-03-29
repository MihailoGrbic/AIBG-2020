from BotStateMachine import BotStateMachine
from utils import *
import actions
from GameState import GameState
from BotExplore import *

class EnemyBotCollectTotemFromCenter(BotStateMachine):

    def get_action_and_state(self, current_game_state: GameState, bot_state):

        self_info = current_game_state.self_info
        curr_tile = current_game_state.map.tiles[self_info.y][self_info.x]

        if bot_state == 'initial':
            if current_game_state.self_info.player_info['initX'] == 0:
                goal = (7, 7)
            else:
                goal = (17, 17)

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
                    current_game_state.internal_bot_state['other_tile_type'] = curr_tile['part']['totemType']
                    if curr_tile['part']['totemType'] != "NEUTRAL":
                        if len(self_info.player_info['parts']) == 3:
                            neutral_part_id = None
                            for part in self_info.player_info['parts']:
                                if part['totemType'] == "NEUTRAL":
                                    neutral_part_id = part['id']
                            return 'other_part_pre_bazar', actions.swap_part(neutral_part_id)
                        else:
                            return 'other_part_pre_bazar', actions.collect()
                    if curr_tile['part']['totemType'] == "NEUTRAL" and len(self_info.player_info['parts']) < 3:
                        return 'first_dig', actions.collect()

            dig_tiles = get_all_non_digged(current_game_state.map, (self_info.x, self_info.y))

            if len(dig_tiles) != 0 and dig_tiles[0][0] == self_info.x and dig_tiles[0][1] == self_info.y:
                del dig_tiles[0]

            if len(dig_tiles) != 0:
                return 'first_dig', get_next_action_towards(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                             (dig_tiles[0][0], dig_tiles[0][1]))
            else:
                return 'first_dig', BotExplore().play_single_turn(current_game_state)

        elif bot_state == "other_part_pre_bazar":

            if near_bazar(self_info):
                if current_game_state.internal_bot_state['other_tile_type'] \
                        in current_game_state.last_report['tradeCenter']['partsTC']:
                    # if in bazar fallback
                    return 'sell', actions.down()
                elif len(self_info.player_info['parts']) == 0:
                    # if already sold by other policy, just revert to initial
                    return 'initial', actions.down()
                else:
                    # continue with chasing
                    return 'other_part', actions.down()

            # go toward bazar
            return 'other_part_pre_bazar', get_next_action_towards(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                                                                   (10,10))

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
                    #fallback to pick any
                    if len(self_info.player_info['parts']) == 3:
                        return 'sell', actions.down()
                    return 'fallback_pick_any', actions.down()

            return 'other_part', get_next_action_towards(current_game_state.map, current_game_state.other_info,
                                                      (self_info.x, self_info.y),
                                                      pos_to_go)

        elif bot_state == 'fallback_pick_any':

            if curr_tile['tileType'] == "DIGTILE":
                if curr_tile["dug"] == False:
                    return 'fallback_pick_any', actions.dig()
                if curr_tile['part'] is not None:
                    if len(self_info.player_info['parts']) == 2:
                        return 'sell', actions.collect()
                    else:
                        return 'fallback_pick_any', actions.collect()

            dig_tiles = get_all_non_digged(current_game_state.map, (self_info.x, self_info.y))

            if len(dig_tiles) != 0 and dig_tiles[0][0] == self_info.x and dig_tiles[0][1] == self_info.y:
                del dig_tiles[0]

            if len(dig_tiles) != 0:
                return 'fallback_pick_any', get_next_action_towards(current_game_state.map, current_game_state.other_info,
                                                            (self_info.x, self_info.y),
                                                            (dig_tiles[0][0], dig_tiles[0][1]))
            else:
                return 'fallback_pick_any', BotExplore().play_single_turn(current_game_state)

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
                return 'find_neutral', BotExplore().play_single_turn(current_game_state)

        elif bot_state == 'sell':
            # bazar_locs = [
            #     (10, 10),
            #     (14, 14),
            #     (10, 14),
            #     (14, 10)
            # ]
            #
            # loc_to_go = min(bazar_locs, key=lambda loc: dist(loc, self_info.pos))

            if near_bazar(self_info) and len(self_info.player_info['parts']) > 0:
                # we're at bazar! sell
                totems = {}
                for part in self_info.player_info['parts']:
                    if part['totemType'] not in totems:
                        totems[part['totemType']] = 0
                    totems[part['totemType']] += 1
                for totem in totems:
                    if totems[totem] == 2 and totem != "NEUTRAL":
                        return 'initial', actions.sell_totem()

                if len(self_info.player_info['parts']) == 1:
                    return 'initial', actions.sell_part(self_info.player_info['parts'][0]['id'])
                else:
                    return 'sell', actions.sell_part(self_info.player_info['parts'][0]['id'])

            if near_bazar(self_info) == 0:
                # another policy already sell
                return 'initial', actions.down()

            return 'sell', get_next_action_towards(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                         (10,10))

