from Bot import Bot
from BotGoTo import BotGoTo
from BotBodyBlock import BotBodyBlock
from BotRandom import BotRandom
from GameState import GameState
from Policy import PolicyAllowOnce, PolicyEnemyFound, PolicyAlwaysAllow


class BotJustBlockShop(Bot):

    def get_policy_list(self):
        return [
            PolicyAllowOnce(BotGoTo(14,14), 1),
            PolicyEnemyFound(BotBodyBlock([[10,10], [10,11], [10,12], [10,13], [10,14], [14,10], [14,11], [14,12], 
            [14,13], [14,14], [11,10], [12,10], [13,10], [11,14], [12,14], [13,14]])),
            PolicyAlwaysAllow(BotRandom())
        ]

    def play_single_turn(self, current_game_state: GameState):
        return self.resolve_policy(current_game_state).play_single_turn(current_game_state)