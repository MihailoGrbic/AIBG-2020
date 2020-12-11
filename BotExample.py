from Bot import Bot
from utils import actions
from GameState import GameState
from BhvrWalker import BhvrWalker

import Policy


class BotBuildSwordAndAttackWithRunaway(Bot):

    def __init__(self):

    def get_policy_list(self):
        return [
            Policy.PolicyAlwaysAllow(BhvrWalker(), 20, 3),
        ]

    def play_single_turn(self, current_game_state: GameState):

        return self.resolve_policy(current_game_state).play_single_turn(current_game_state)
