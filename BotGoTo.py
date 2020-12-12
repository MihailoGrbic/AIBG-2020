from Bot import Bot
from GameState import GameState
from utils import astar, move_once
import actions


class BotGoTo(Bot):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def play_single_turn(self, current_game_state: GameState):
        return move_once(current_game_state, target=(self.x, self.y))

