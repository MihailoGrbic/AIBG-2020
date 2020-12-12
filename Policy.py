from Bot import Bot
from GameState import GameState
import utils
import random


class Policy:
    def __init__(self, bot: Bot):
        self.bot = bot

    def should_execute(self, current_game_state: GameState):
        pass


class PolicyAlwaysAllow(Policy):
    def should_execute(self, current_game_state: GameState):
        print("PolicyAlwaysAllow " + str(True))
        return True

class PolicyAllowOnce(Policy):
    def __init__(self, Bot: Bot, policy_id):
        Policy.__init__(self, Bot)
        self.policy_id = policy_id

    def should_execute(self, current_game_state: GameState):
        
        if self.policy_id not in current_game_state.internal_bot_state:
            if self.bot.finished(current_game_state):
                current_game_state.internal_bot_state[self.policy_id] = "Finished"
                print(current_game_state.internal_bot_state[self.policy_id])
                return False
            return True
        else:
            return False

class PolicyEnemyFound(Policy):
    def should_execute(self, current_game_state: GameState):
        print(current_game_state.opponent_visible)
        return current_game_state.opponent_visible

