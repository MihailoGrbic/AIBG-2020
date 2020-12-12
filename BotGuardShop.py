from Bot import Bot
from BotGoTo import BotGoTo
from utils import *

class BotGuardShop(Bot):

    def __init__(self):
        self.target_index = 0

    def play_single_turn(self, current_game_state):
        initX = current_game_state.self_info.player_info['initX']
        initY = current_game_state.self_info.player_info['initY']

        targets = [[10, 10], [10, 14], [14, 12]]

        if current_game_state.turns_left >= 2000-150:
            if initX == 0:
                targets = [[14, 11], [14, 13]]
            else:
                targets = [[10, 11], [10, 13]]

        if current_game_state.turns_left >= 2000-100:
            print(current_game_state.turns_left)
            if initX == 0:
                targets = [[14, 14], [14, 13]]
            else:
                targets = [[10, 10], [10, 11]]

        # print(targets)

        x = current_game_state.self_info.x
        y = current_game_state.self_info.y

        if [x, y] == targets[self.target_index]:
            self.target_index += 1
            if self.target_index == len(targets):
                self.target_index = 0
        print("dosao")
        # print(targets)
        # print(targets[self.target_index])
        target = targets[self.target_index]
        if "RememberEnemyPosition" in current_game_state.internal_bot_state and current_game_state.internal_bot_state["TurnsSinceSeenEnemy"] < 8:
            print("dosao sam ovde1")
            print(current_game_state.internal_bot_state["RememberEnemyPosition"])
            closest = find_closest_coordinate(current_game_state.internal_bot_state["RememberEnemyPosition"], shopping_tiles, current_game_state.map, current_game_state.other_info)
            print("wtf")
            print(closest)
            target = closest
            print("dosao sam ovde")
        return move_once(current_game_state, target = (target[0], target[1]))
