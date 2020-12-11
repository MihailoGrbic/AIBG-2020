from Bot import Bot
from GameState import GameState
from utils import actions


class BotRotate(Bot):

    def __init__(self):
        self.counter = 0

    def play_single_turn(self, current_game_state: GameState):
        self.counter += 1
        self.counter %= 4
        if self.counter == 0:
            return actions["LEFT"]
        if self.counter == 1:
            return actions["UP"]
        if self.counter == 2:
            return actions["RIGHT"]
        if self.counter == 3:
            return actions["DOWN"]
