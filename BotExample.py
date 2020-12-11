from Bot import Bot
from utils import actions
from GameState import GameState
from BehaviourWalker import BehaviourWalker

import Policy


class BotBuildSwordAndAttackWithRunaway(Bot):

    def __init__(self):
        pass

    def get_policy_list(self):
        return [
            Policy.PolicyAlwaysAllow(BehaviourWalker(), 20, 3),
        ]

    def play_single_turn(self, current_game_state: GameState):

        return self.resolve_policy(current_game_state).play_single_turn(current_game_state)
