from Bot import Bot
from GameState import GameState
import actions

class BotRotate(Bot):

    def __init__(self):
        self.counter = 0

    def play_single_turn(self, current_game_state: GameState):
        self.counter += 1
        self.counter %= 4
        if self.counter == 0:
            return actions.left()
        if self.counter == 1:
            return actions.up()
        if self.counter == 2:
            return actions.right()
        if self.counter == 3:
            return actions.down()
