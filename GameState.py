from Map import Map
from PlayerInfo import PlayerInfo
from utils import get_symetric_pos


class GameState(object):
    def __init__(self, res, gameId, playerId):
        self.playerId = playerId
        self.gameId = gameId
        self.game_state = res
        self.turns_left = res['turn']
        self.map = Map(res)
        self.self_info = PlayerInfo(res['nextPlayerObject'])
        self.other_info = PlayerInfo(res['otherPlayerObject'])
        self.opponent_visible = False
        self.internal_bot_state = {}
        self.totem_locations = {10 * i + j: None for i in range(1, 8) for j in [1, 2]}.update(
            {80 + i: None for i in range(7)}
        )  # Locations of each totem by its totem id

    def update_game_state(self, report):

        self.update_totem_locations(report)

        self.self_info = PlayerInfo(report['nextPlayerObject'])
        if bool(report['otherPlayerObject']):
            self.other_info = PlayerInfo(report['otherPlayerObject'])
            self.opponent_visible = True
            x = self.other_info.x
            y = self.other_info.y
            r_x, r_y = self.map.reverse_corr(x, y)
            if self.other_info.player_info['scorpionPoison']:
                self.map.mark_trap(x, y, 'SCORPION')
                self.map.mark_trap(r_x, r_y, 'SCORPION')

            if self.other_info.player_info['trappedInQuickSand']:
                self.map.mark_trap(x, y, 'QUICKSAND')
                self.map.mark_trap(r_x, r_y, 'QUICKSAND')

        else:
            self.opponent_visible = False

        for row in report['map']['tiles']:
            for tile in row:
                if bool(tile):
                    x = tile['x']
                    y = tile['y']
                    r_x, r_y = self.map.reverse_corr(x, y)
                    self.map.update_tile(tile)
                    self.map.update_tile_reverse(r_x, r_y, tile)

                    if 'trap' in tile and bool(tile['trap']):
                        if tile['trap']['visible']:
                            r_x, r_y = self.map.reverse_corr(x, y)
                            self.map.mark_trap(x, y, tile['trap']['trapType'])
                            self.map.mark_trap(r_x, r_y, tile['trap']['trapType'])

    def update_totem_locations(self, report):
        for y, row in enumerate(self.map.tiles):
            for x, tile in enumerate(row):
                # if (x, y) in self.totem_locations.values():
                if "tileType" in tile and tile["tileType"] is "DIGTILE" and tile["dug"] is True:
                    part_id = tile["part"].get("id", None)
                    for found_part, pos in self.totem_locations.items():
                        if found_part != part_id:
                            self.totem_locations[found_part] = pos
                            self.totem_locations[part_id] = "Moved"

                if "part" in tile and tile["part"] is not None and "id" in tile["part"]:
                    totem_id = tile["part"]["id"]
                    print(self.totem_locations)
                    self.totem_locations[totem_id] = (tile["x"], tile["y"])
                    diff = 1 if totem_id % 2 == 1 else -1
                    if self.totem_locations[totem_id + diff] is None:
                        self.totem_locations[totem_id + diff] = self.map.reverse_corr(tile["x"], tile["y"])

        if "tradeCenter" in report and "partsTC" in report["tradeCenter"]:
            for part in report["tradeCenter"]["partsTC"]:
                self.totem_locations[part["id"]] = "Shop"
