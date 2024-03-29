from Bot import Bot
from GameState import GameState
from utils import *
import random
import math
from utils import shopping_tiles, find_path_to, astar_dist

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
                return False
            return True
        else:
            return False

class PolicyEnemyFound(Policy):
    def should_execute(self, current_game_state: GameState):
        return current_game_state.opponent_visible

class PolicyEnemyNearby(Policy):
    def __init__(self, Bot: Bot, turn_tolerance = 4):
        Policy.__init__(self, Bot)
        self.turn_tolerance = turn_tolerance

    def should_execute(self, current_game_state: GameState):
        if "ExpectedEnemyPosition" not in current_game_state.internal_bot_state:
            return False
        enemy_pos = current_game_state.internal_bot_state["ExpectedEnemyPosition"]
        perceived_distance = astar_dist((current_game_state.self_info.x, current_game_state.self_info.y), (enemy_pos[0], enemy_pos[1]), current_game_state.map, current_game_state.other_info)
        return perceived_distance < 5 and current_game_state.internal_bot_state["TurnsSinceSeenEnemy"] < self.turn_tolerance
        
class PolicyEnemyQuicksand(Policy):
    def should_execute(self, current_game_state: GameState):
        return current_game_state.opponent_visible and current_game_state.other_info.player_info["trappedInQuickSand"]
class PolicyPartNumber(Policy):
    # Executes if a bot needs more or less parts, if want_more is true any number of items less than the ideal 
    # number will trigger this policy, while the opposite is true if want_more is false
    def __init__(self, Bot: Bot, ideal_parts = 1, want_more = True):
        Policy.__init__(self, Bot)
        self.ideal_parts = ideal_parts
        self.want_more = want_more

    def should_execute(self, current_game_state: GameState):
        if current_game_state.self_info.player_info["money"] > 0:
            return False
        if self.want_more:
            return len(current_game_state.self_info.player_info['parts']) < self.ideal_parts
        else:
            return len(current_game_state.self_info.player_info['parts']) > self.ideal_parts

class PolicyCantSellNextTurn(Policy):
    def __init__(self, Bot: Bot):
        Policy.__init__(self, Bot)

    def should_execute(self, current_game_state: GameState):
        turns_left = math.ceil(current_game_state.turns_left / 2)

        min_path = 100
        for tile in shopping_tiles:
            path = find_path_to(current_game_state.self_info, current_game_state.other_info, current_game_state.map, tile[0], tile[1])
            if min_path > len(path) + 2:
                min_path = len(path) + 2

        if min_path > turns_left: print("Cant sell next turn")
        return min_path > turns_left


class PolicyNearBazarCanMakeTotem(Policy):
    def __init__(self, Bot: Bot):
        Policy.__init__(self, Bot)

    def should_execute(self, current_game_state: GameState):
        self_info = current_game_state.self_info
        if not near_bazar(self_info):
            return False

        totems = {}
        for part in self_info.player_info['parts']:
            if part['totemType'] not in totems:
                totems[part['totemType']] = 0
            totems[part['totemType']] += 1
        for totem in current_game_state.last_report['tradeCenter']['partsTC']:
            if totem['totemType'] not in totems:
                totems[totem['totemType']] = 0
            totems[totem['totemType']] += 1

        totem_to_buy = None
        for totemType in totems:
            if totemType == "NEUTRAL":
                continue
            if totems[totemType] == 2 and 'NEUTRAL' in totems:
                totem_to_buy = totemType

        have_money_for_totem = len(self_info.player_info['parts']) == 3
        have_money_for_totem = have_money_for_totem or (len(self_info.player_info['parts']) == 2 and self_info.player_info['money'] >= 450)
        have_money_for_totem = have_money_for_totem or (len(self_info.player_info['parts']) == 1 and self_info.player_info['money'] >= 900)
        have_money_for_totem = have_money_for_totem or (len(self_info.player_info['parts']) == 0 and self_info.player_info['money'] >= 1350)

        return totem_to_buy is not None and have_money_for_totem





class PolicyBodyBlockFallback(Policy):
    def __init__(self, Bot: Bot):
        Policy.__init__(self, Bot)

    def should_execute(self, current_game_state: GameState):

        if "money" in current_game_state.other_info.player_info \
        and current_game_state.self_info.player_info["money"] < current_game_state.other_info.player_info["money"]:
            return True

        if current_game_state.self_info.player_info["health"] < 50 \
        and current_game_state.self_info.player_info["health"] < current_game_state.other_info.player_info["health"]:
            return True

        if [current_game_state.other_info.x, current_game_state.other_info.y] in shopping_tiles \
        and len(current_game_state.other_info.player_info["parts"]) > 0 \
        and current_game_state.self_info.player_info["health"] < current_game_state.other_info.player_info["health"]:
            return True

class PolicyNoProgress(Policy):
    def __init__(self, Bot: Bot):
        Policy.__init__(self, Bot)

    def should_execute(self, current_game_state: GameState):

        if 'lru_positions' not in current_game_state.internal_bot_state:
            current_game_state.internal_bot_state['lru_positions'] = []

        if len(current_game_state.internal_bot_state['lru_positions']) == 10:
            del current_game_state.internal_bot_state['lru_positions'][0]

        current_game_state.internal_bot_state['lru_positions'].append(current_game_state.self_info.pos)

        positions = {}
        for pos in current_game_state.internal_bot_state['lru_positions']:
            if pos not in positions:
                positions[pos] = 0
            positions[pos] += 1

        return len(current_game_state.internal_bot_state['lru_positions']) == 10 and len(positions) <= 3

