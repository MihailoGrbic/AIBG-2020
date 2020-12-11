from Bot import Bot
import actions
import random

class BotRandom(Bot):

    def play_single_turn(self, current_game_state):
        action_list = [actions.left(), actions.right(), actions.up(), actions.down()]
        return action_list[random.randrange(4)]
