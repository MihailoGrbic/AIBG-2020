from __future__ import annotations
from Client import *
from GameState import GameState
from Map import Map
from PlayerInfo import PlayerInfo
import pprint
import actions


class Bot(object):

    def play_single_turn(self, current_game_state: GameState):
        pass

    def get_policy_list(self):
        return list()

    def resolve_policy(self, current_game_state: GameState) -> Bot:
        for policy in self.get_policy_list():
            if policy.should_execute(current_game_state):
                return policy.bot
        return None
