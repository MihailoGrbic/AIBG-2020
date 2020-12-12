from Bot import Bot
from GameState import GameState
import actions
from utils import move_available
import random

class BotRandom(Bot):
    def __init__(self):
        self.counter = 0

    def play_single_turn(self, current_game_state):
        action_list = []
        if move_available(current_game_state.map, current_game_state.other_info, (current_game_state.x + 1, current_game_state.y)):
            action_list.append(actions.right())
        if move_available(current_game_state.map, current_game_state.other_info, (current_game_state.x - 1, current_game_state.y)):
            action_list.append(actions.left())
        if move_available(current_game_state.map, current_game_state.other_info, (current_game_state.x, current_game_state.y + 1)):
            action_list.append(actions.down())
        if move_available(current_game_state.map, current_game_state.other_info, (current_game_state.x, current_game_state.y - 1)):
            action_list.append(actions.up())
        return action_list[random.randrange(len(action_list))]
