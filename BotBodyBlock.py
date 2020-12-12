from Bot import Bot
from utils import *

class BotBodyBlock(Bot):

    def __init__(self, blocked_tiles, expected_jukes = "safe"):
        self.counter = 0
        self.blocked_tiles = blocked_tiles
        self.expected_jukes = expected_jukes

    def play_single_turn(self, current_game_state):
        self_x = current_game_state.self_info.player_info["x"]
        self_y = current_game_state.self_info.player_info["y"]
        if current_game_state.opponent_visible:
            enemy_x = current_game_state.other_info.player_info["x"]
            enemy_y = current_game_state.other_info.player_info["y"]
            current_game_state.internal_bot_state["RememberEnemyPosition"] = [enemy_x, enemy_y]
            current_game_state.internal_bot_state["ExpectedEnemyPosition"] = current_game_state.internal_bot_state["RememberEnemyPosition"]
            current_game_state.internal_bot_state["TurnsSinceSeenEnemy"] = 0
        else:
            current_game_state.internal_bot_state["TurnsSinceSeenEnemy"] += 1
            if current_game_state.internal_bot_state["ExpectedEnemyPosition"][1] > 17:
                if self.expected_jukes == "safe":
                    if current_game_state.internal_bot_state["ExpectedEnemyPosition"][0] < self_x:
                        current_game_state.internal_bot_state["ExpectedEnemyPosition"][0] -= 1
                    else:
                        current_game_state.internal_bot_state["ExpectedEnemyPosition"][0] += 1

                if self.expected_jukes == "risky":
                    current_game_state.internal_bot_state["ExpectedEnemyPosition"][1] += 1
                    

            if current_game_state.internal_bot_state["ExpectedEnemyPosition"][1] < 8:
                if self.expected_jukes == "safe":
                    if current_game_state.internal_bot_state["ExpectedEnemyPosition"][0] < self_x:
                        current_game_state.internal_bot_state["ExpectedEnemyPosition"][0] -= 1
                    else:
                        current_game_state.internal_bot_state["ExpectedEnemyPosition"][0] += 1

                if self.expected_jukes == "risky":
                    current_game_state.internal_bot_state["ExpectedEnemyPosition"][1] -= 1


            if current_game_state.internal_bot_state["ExpectedEnemyPosition"][0] > 17:
                if self.expected_jukes == "safe":
                    if current_game_state.internal_bot_state["ExpectedEnemyPosition"][1] < self_y:
                        current_game_state.internal_bot_state["ExpectedEnemyPosition"][1] -= 1
                    else:
                        current_game_state.internal_bot_state["ExpectedEnemyPosition"][1] += 1

                if self.expected_jukes == "risky":
                    current_game_state.internal_bot_state["ExpectedEnemyPosition"][0] += 1
            
            if current_game_state.internal_bot_state["ExpectedEnemyPosition"][0] < 8:
                if self.expected_jukes == "safe":
                    if current_game_state.internal_bot_state["ExpectedEnemyPosition"][1] < self_y:
                        current_game_state.internal_bot_state["ExpectedEnemyPosition"][1] -= 1
                    else:
                        current_game_state.internal_bot_state["ExpectedEnemyPosition"][1] += 1

                if self.expected_jukes == "risky":
                    current_game_state.internal_bot_state["ExpectedEnemyPosition"][0] -= 1


        [enemy_x, enemy_y] = current_game_state.internal_bot_state["ExpectedEnemyPosition"]
        left_target = [enemy_y, enemy_x - 1, 0]
        right_target = [enemy_y, enemy_x + 1, 0]
        above_target = [enemy_y - 1, enemy_x, 0]
        bellow_target = [enemy_y + 1, enemy_x, 0]

        while not move_available(current_game_state.map, current_game_state.other_info, (left_target[1], left_target[0])):
            left_target[1] -= 1
            if left_target[1] < 0:
                break
        while not move_available(current_game_state.map, current_game_state.other_info, (right_target[1], right_target[0])):
            right_target[1] += 1
            if right_target[1] > 24:
                break
        while not move_available(current_game_state.map, current_game_state.other_info, (above_target[1], above_target[0])):
            above_target[0] -= 1
            if above_target[0] < 0 :
                break
        while not move_available(current_game_state.map, current_game_state.other_info, (bellow_target[1], bellow_target[0])):
            bellow_target[0] += 1  
            if bellow_target[0] > 24:
                break        

        for tile in self.blocked_tiles:
            if tile[1] <= left_target[1]: left_target[2] +=1
            if tile[1] >= right_target[1]: right_target[2] +=1
            if tile[0] <= above_target[0]: above_target[2] +=1
            if tile[0] >= bellow_target[0]: bellow_target[2] +=1

        final_target = left_target
        for target in [right_target, above_target, bellow_target]:
            if final_target[2] < target[2]:
                final_target = target
    
        final_target = (final_target[1], final_target[0])
        print(final_target)
        return move_once(current_game_state, final_target)




