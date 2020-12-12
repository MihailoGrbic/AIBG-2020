# from utils import *

# Example dict:


class PlayerInfo(object):
    def __init__(self, player1):
        # TODO (djokjulapfe): nisam siguran kako ovo player1/2 radi
        self.player_info = player1
        if bool(player1):
            self.x = self.player_info['x']
            self.y = self.player_info['y']
        else:
            self.x = -1
            self.y = -1
        self.pos = (self.x, self.y)
