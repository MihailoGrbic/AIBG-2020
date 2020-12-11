from Bot import Bot
from GameState import GameState
import actions
import random

class BotRandom(Bot):
    def __init__(self):
        self.counter = 0

    def play_single_turn(self, current_game_state):
        action_list = [actions.left(), actions.right(), actions.up(), actions.down()]
        return action_list[random.randrange(4)]
