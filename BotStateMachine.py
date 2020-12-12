from Bot import Bot
from utils import *


class BotStateMachine(Bot):

    def play_single_turn(self, current_game_state: GameState):
        if 'bot_state' not in current_game_state.internal_bot_state:
            current_game_state.internal_bot_state['bot_state'] = 'initial'

        action, next_state = self.get_action_and_state(current_game_state, current_game_state.internal_bot_state['bot_state'])
        print(f"last_state: {current_game_state.internal_bot_state['bot_state']}, next_state: {next_state}, action: {action}")

        current_game_state.internal_bot_state['bot_state'] = next_state
        return action

    def get_action_and_state(self, current_game_state, bot_state):
        pass





