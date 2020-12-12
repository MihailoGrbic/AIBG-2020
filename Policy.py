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
        return current_game_state.opponent_visible

class PolicyPartNumber(Policy):
    # Executes if a bot needs more or less parts, if want_more is true any number of items less than the ideal 
    # number will trigger this policy, while the opposite is true if want_more is false
    def __init__(self, Bot: Bot, ideal_parts = 1, want_more = True):
        Policy.__init__(self, Bot)
        self.ideal_parts = ideal_parts
        self.want_more = want_more

    def should_execute(self, current_game_state: GameState):
        if self.want_more:
            return len(current_game_state.self_info.player_info['parts']) < self.ideal_parts
        else:
            return len(current_game_state.self_info.player_info['parts']) > self.ideal_parts
        
