from Bot import Bot
from GameState import GameState
from utils import astar
import actions


class BotGoTo(Bot):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def play_single_turn(self, current_game_state: GameState):
        self_info = current_game_state.self_info
        self_pos = self_info.x, self_info.y
        print(self_pos)
        path = astar(current_game_state.map, current_game_state.other_info, self_pos, (self.x, self.y))
        print(path[1])
        x_diff = path[1][0] - self_info.x
        y_diff = path[1][1] - self_info.y
        if x_diff == 1:
            return actions.right()
        if x_diff == -1:
            return actions.left()
        if y_diff == 1:
            return actions.down()
        return actions.up()
