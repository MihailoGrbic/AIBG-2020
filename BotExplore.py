from Bot import Bot
from GameState import GameState
from utils import *
from actions import move_actions


class BotExplore(Bot):

    def play_single_turn(self, current_game_state: GameState):
        discoveries = get_discovery_tiles_per_direction(current_game_state.map, current_game_state.self_info)
        for direction in move_actions:
            if not move_available(current_game_state.map, current_game_state.other_info, add_vector(current_game_state.self_info.pos, dir_to_diff[direction])):
                discoveries[direction] = 0
        best_action = max(move_actions, key=lambda direction: discoveries[direction])
        print(best_action)
        if discoveries[best_action] != 0:
            return best_action

        current_map = current_game_state.map
        possible_targets = get_all_undiscovered_tiles(current_game_state.map)
        if len(possible_targets) == 0:
            print("The whole world is explored, I'll just wonder aimlessly...")
            self_info = current_game_state.self_info
            if self_info.x == 10 and self_info.y == 10:
                return random_movement_action()
            else:
                return get_next_action_towards(current_game_state.map, current_game_state.other_info, (self_info.x, self_info.y),
                         (10,10))

        target = find_closest_undiscovered(current_map, current_game_state.other_info, possible_targets, current_game_state.self_info.pos)
        print("target for exploring: ", target)
        return move_once(current_game_state, target)
