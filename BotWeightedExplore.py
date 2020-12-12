from Bot import Bot
from GameState import GameState
from utils import *
from actions import move_actions
from PlayerInfo import PlayerInfo
from typing import Optional, Callable


class BotWeightedExplore(Bot):

    def __init__(self, positional_scoring: Optional[Callable[[tuple], int]] = None):
        if positional_scoring is None:
            self.positional_scoring = self.central_distance_scoring
        else:
            self.positional_scoring = positional_scoring

    @staticmethod
    def central_distance_scoring(pos: tuple) -> int:
        diff = sub_vector((12, 12), pos)
        # return 1
        return 50 - abs(diff[0]) - abs(diff[1])

    def play_single_turn(self, current_game_state: GameState):
        for j, row in enumerate(current_game_state.map.tiles):
            for i, tile in enumerate(row):
                if tile.get("DISCOVERED", False):
                    print("O ", end="")
                else:
                    score = self.positional_scoring((j, i))
                    print(f"{score % 10} ", end="")
            print()

        discoveries = self.get_discovery_tile_values_per_direction(current_game_state.map, current_game_state.self_info)
        for direction in move_actions:
            if not move_available(current_game_state.map, current_game_state.other_info,
                                  add_vector(current_game_state.self_info.pos, dir_to_diff[direction])):
                discoveries[direction] = 0
        best_action = max(move_actions, key=lambda direction: discoveries[direction])
        if discoveries[best_action] != 0:
            return best_action

        current_map = current_game_state.map
        possible_targets = get_all_undiscovered_tiles(current_game_state.map)
        if len(possible_targets) == 0:
            print("The whole world is explored, I'll just wonder aimlessly...")
            return random_movement_action()

        target = find_closest_undiscovered(current_map, current_game_state.other_info, possible_targets,
                                           current_game_state.self_info.pos)
        return move_once(current_game_state, target)

    def get_discovery_tile_values_per_direction(self, current_map, current_pos: PlayerInfo):
        # TODO: update vision when possible
        vision_radius = 3
        solution = dict()
        solution[actions.up()] = self.calc_unknown_tile_scores(current_map, (current_pos.x, current_pos.y - 1), vision_radius)
        solution[actions.down()] = self.calc_unknown_tile_scores(current_map, (current_pos.x, current_pos.y + 1), vision_radius)
        solution[actions.left()] = self.calc_unknown_tile_scores(current_map, (current_pos.x - 1, current_pos.y), vision_radius)
        solution[actions.right()] = self.calc_unknown_tile_scores(current_map, (current_pos.x + 1, current_pos.y), vision_radius)
        print(solution)
        return solution

    def calc_unknown_tile_scores(self, current_map, current_pos, vision_radius):
        score = 0
        # vision_radius += 1
        for i in range(vision_radius + 1):
            for j in range(vision_radius + 1):
                x = i - j + current_pos[0]
                y = i + j - vision_radius + current_pos[1]
                if within_bounds(current_map, (x, y)) and not current_map.tiles[y][x].get("DISCOVERED", False):
                    score += self.positional_scoring((x, y))
        return score

