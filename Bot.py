from Client import *
from GameState import GameState
from Map import Map
from PlayerInfo import PlayerInfo
import pprint
import actions


class Bot(object):

    def play_single_turn(self, current_game_state: GameState):
        pass

    def get_policy_list(self, current_game_state: GameState):
        return list()

    def resolve_policy(self, current_game_state: GameState):
        for policy in self.get_policy_list(current_game_state):
            if policy.should_execute(current_game_state):
                print("Policy resolved: ", type(policy))
                return policy.bot
        return None
