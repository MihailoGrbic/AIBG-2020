from Bot import Bot
from BotGoTo import BotGoTo
from BotBodyBlock import BotBodyBlock
from BotRandom import BotRandom
from BotRushOnePart import BotRushOnePart
from BotGuardShop import BotGuardShop
from BotSellAll import BotSellAll
from GameState import GameState
from Policy import *
from utils import shopping_tiles
from BotSellTotem import BotSellTotem
from EnemyBotCollectTotemFromCenter import *


class BotPolicyCollectTotem(Bot):
    def __init__(self, expected_jukes="safe"):
        self.expected_jukes = expected_jukes

    def get_policy_list(self, current_game_state: GameState):
        policy_list = []
        policy_list.append(PolicyNoProgress(BotRandom()))
        policy_list.append(PolicyNearBazarCanMakeTotem(BotSellTotem()))
        policy_list.append(PolicyAlwaysAllow(EnemyBotCollectTotemFromCenter()))

        # policy_list.append(PolicyAlwaysAllow(BotGuardShop()))
        return policy_list

    def play_single_turn(self, current_game_state: GameState):
        return self.resolve_policy(current_game_state).play_single_turn(current_game_state)
