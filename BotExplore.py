from Bot import Bot
from GameState import GameState
from utils import get_all_undiscovered_tiles, find_closest_coordinate, move_once, random_movement_action, \
    get_discovery_tiles_per_direction
from BotGoTo import BotGoTo
from Policy import PolicyAlwaysAllow
from actions import move_actions


class BotExplore(Bot):

    def play_single_turn(self, current_game_state: GameState):
        discoveries = get_discovery_tiles_per_direction(current_game_state.map, current_game_state.self_info.pos)
        best_action = min(move_actions, key=lambda direction: discoveries[direction])
        if discoveries[best_action] != 0:
            return best_action

        possible_targets = get_all_undiscovered_tiles(current_game_state.map)
        if len(possible_targets) == 0:
            print("The whole world is explored, I'll just wonder aimlessly...")
            return random_movement_action()
        target = find_closest_coordinate(current_game_state.self_info.pos, possible_targets)
        return move_once(current_game_state, target)
