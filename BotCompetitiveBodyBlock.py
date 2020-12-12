from Bot import Bot
from BotGoTo import BotGoTo
from BotBodyBlock import BotBodyBlock
from BotRandom import BotRandom
from BotRushOnePart import BotRushOnePart
from BotGuardShop import BotGuardShop
from BotLastMinuteSell import BotLastMinuteSell
from GameState import GameState
from Policy import PolicyAllowOnce, PolicyEnemyFound, PolicyAlwaysAllow, PolicyPartNumber


class BotJustBlockShop(Bot):
    def __init__(self, blocked_tiles, expected_jukes = "safe"):
        self.expected_jukes = expected_jukes

    def get_policy_list(self, current_game_state: GameState):
        policy_list = []
        policy_list.append(PolicyPartNumber(BotRushOnePart))
        policy_list.append(
            PolicyEnemyFound(BotBodyBlock([[10,10], [10,11], [10,12], [10,13], [10,14], [14,10], [14,11], 
            [14,12], [14,13], [14,14], [11,10], [12,10], [13,10], [11,14], [12,14], [13,14]], self.expected_jukes)))
        policy_list.append(PolicyAlwaysAllow(BotGuardShop()))
        return policy_list

    def play_single_turn(self, current_game_state: GameState):
        return self.resolve_policy(current_game_state).play_single_turn(current_game_state)