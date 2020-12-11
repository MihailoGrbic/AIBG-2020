from Bot import Bot
from BotRunnaway import BotRunnaway
import GameState
import utils
from GameState import GameState
from BotResourceGather import BotResourceGatherer
import utils
import random


class Policy:
    def __init__(self, bot: bot):
        self.bot = bot

    def should_execute(self, current_game_state: GameState):
        pass


class PolicyAlwaysAllow(Policy):
    def should_execute(self, current_game_state: GameState):
        print("PolicyAlwaysAllow " + str(True))
        return True

class EnemyFound(Policy):
    def should_execute(self, current_game_state: GameState):
        return GameState.enemy_visible


