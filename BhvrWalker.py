from Bot import Bot
import utils
from PlayerInfo import PlayerInfo


class BhvrWalker(Bot):

    def __init__(self, x=-1, y=-1):
        self.x_sel = x
        self.y_sel = y

    def play_single_turn(self, current_game_state):
        path = utils.find_path_to(current_game_state.self_info, current_game_state.other_info, current_game_state.map,
                                  self.x_sel, self.y_sel)
        if path is not None:
            return path[0]
