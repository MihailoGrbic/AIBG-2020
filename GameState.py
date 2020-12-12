from Map import Map
from PlayerInfo import PlayerInfo


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


    def update_game_state(self, report):

        self.self_info = PlayerInfo(report['nextPlayerObject'])
        if bool(report['otherPlayerObject']):
            self.other_info = PlayerInfo(report['otherPlayerObject'])
            self.opponent_visible = True
            x = self.other_info['x']
            y = self.other_info['y']
            r_x, r_y = self.map.reverse_corr(x, y)
            if self.other_info['scorpionPoison']:

                self.map.mark_trap(x, y,'SCORPION')
                self.map.mark_trap(r_x, r_y,'SCORPION')

            if self.other_info['trappedInQuickSand']:
                self.map.mark_trap(x, y,'QUICKSAND')
                self.map.mark_trap(r_x, r_y,'QUICKSAND')

        else:
            self.opponent_visible = False

        for row in report['map']['tiles']:
            for tile in row:
                if bool(tile):
                    x = tile['x']
                    y = tile['y']
                    self.map.update_tile(tile)

                    if 'trap' in tile and bool(tile['trap']):
                        if tile['trap']['visible']:
                            r_x, r_y = self.map.reverse_corr(x, y)
                            self.map.mark_trap(x,y,tile['trap']['trapType'])
                            self.map.mark_trap(r_x,r_y,tile['trap']['trapType'])
