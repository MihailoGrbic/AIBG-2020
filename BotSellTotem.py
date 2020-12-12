from Bot import Bot
from BotGoTo import BotGoTo
from utils import *


class BotSellTotem(Bot):

    def play_single_turn(self, current_game_state):

        self_info = current_game_state.self_info

        totems = {}
        player_totems = {}
        for part in self_info.player_info['parts']:
            if part['totemType'] not in totems:
                totems[part['totemType']] = 0
            totems[part['totemType']] += 1
            if part['totemType'] not in player_totems:
                player_totems[part['totemType']] = 0
            player_totems[part['totemType']] += 1
        for totem in current_game_state.last_report['tradeCenter']['partsTC']:
            if totem['totemType'] not in totems:
                totems[totem['totemType']] = 0
            totems[totem['totemType']] += 1

        totem_to_buy = None
        # try to find the totem which we have two parts for
        for totemType in totems:
            if totemType == "NEUTRAL":
                continue
            if totems[totemType] == 2 and 'NEUTRAL' in totems and totemType in player_totems and player_totems[totemType] == 2:
                totem_to_buy = totemType

        if totem_to_buy is None:
            # try to find the totem which we have one part for
            for totemType in totems:
                if totemType == "NEUTRAL":
                    continue
                if totems[totemType] == 2 and 'NEUTRAL' in totems and totemType in player_totems and player_totems[totemType] == 1:
                    totem_to_buy = totemType

            if totem_to_buy is None:
                # try to find any totem
                for totemType in totems:
                    if totemType == "NEUTRAL":
                        continue
                    if totems[totemType] == 2 and 'NEUTRAL' in totems:
                        totem_to_buy = totemType

        return resolve_trade_action(
            self_info.player_info['parts'],
            current_game_state.last_report['tradeCenter']['partsTC'],
            totem_to_buy)


