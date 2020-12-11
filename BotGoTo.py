from Bot import Bot
from GameState import GameState
from utils import actions, astar


class BotGoTo(Bot):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def play_single_turn(self, current_game_state: GameState):
        self_info = current_game_state.self_info.player_info
        path = astar(current_game_state.map, current_game_state.other_info, (self_info['x'], self_info['y']), (self.x, self.y))
        x_diff = path[1][0] - self_info.x
        y_diff = path[1][1] - self_info.y
        if x_diff == 1:
            return actions["RIGHT"]
        if x_diff == -1:
            return actions["LEFT"]
        if y_diff == 1:
            return actions["DOWN"]
        return actions["UP"]
