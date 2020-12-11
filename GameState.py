from Map import Map
from PlayerInfo import PlayerInfo


class GameState(object):
    def __init__(self, res, gameId, playerId):
        self.playerId = playerId
        self.gameId = gameId
        self.game_state = res
        self.turns_left = res['turn']
        self.map = Map(res)
        self.self_info = PlayerInfo(res, player1=res['nextPlayerObject'])
        self.other_info = PlayerInfo(res, player1=res['otherPlayerObject'])
        self.opponent_visible = False

    def update_game_state(self, report):

        self.self_info = PlayerInfo(report, player1=report['nextPlayerObject'])
        if bool(report['otherPlayerObject']):
            self.other_info = PlayerInfo(report, player1=report['otherPlayerObject'])
            self.opponent_visible = True
        else:
            self.opponent_visible = False

        for row in report['map']['tiles']:
            for tile in row:
                if bool(tile):
                    x = tile['x']
                    y = tile['y']
                    self.map.tiles[y][x] = tile

                    # if bool(tile['trap']):
                    #     r_x, r_y = Map.reverse_corr(x, y)
                    #     self.map.tiles[r_y][r_x] = tile
                    #     self.map.tiles[r_y][r_x]['x'] = r_x
                    #     self.map.tiles[r_y][r_x]['y'] = r_y