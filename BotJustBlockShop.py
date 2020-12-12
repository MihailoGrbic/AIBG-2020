from Bot import Bot
from BotGoTo import BotGoTo
from BotBodyBlock import BotBodyBlock
from BotRandom import BotRandom
from GameState import GameState
from Policy import PolicyAllowOnce, PolicyEnemyFound, PolicyAlwaysAllow
from utils import shopping_tiles


class BotJustBlockShop(Bot):

    def get_policy_list(self, current_game_state: GameState):
        policy_list = []
        if current_game_state.self_info.x == 0:
            policy_list.append(PolicyAllowOnce(BotGoTo(14,14), 1))
        else:
            policy_list.append(PolicyAllowOnce(BotGoTo(10,10), 1))

        policy_list.append(
            PolicyEnemyFound(BotBodyBlock(shopping_tiles)))
        policy_list.append(PolicyAlwaysAllow(BotRandom()))
        
        return policy_list

    def play_single_turn(self, current_game_state: GameState):
        return self.resolve_policy(current_game_state).play_single_turn(current_game_state)