# from utils import *

# Example dict:
# {'buildings': [],
#  'health': 100,
#  'id': 1,
#  'initX': 0,
#  'initY': 0,
#  'kills': 0,
#  'lives': 5,
#  'notFinishedBuildings': [],
#  'resources': {'METAL': 0, 'STONE': 0, 'WOOD': 0},
#  'score': 0,
#  'stringType': 'Player',
#  'stupidMoves': 7,
#  'weapon1': None,
#  'weapon2': None,
#  'x': 3,
#  'y': 2}


class PlayerInfo(object):
    def __init__(self, res, player1):
        # TODO (djokjulapfe): nisam siguran kako ovo player1/2 radi
        self.player_info = player1
        if bool(player1):
            self.x = self.player_info['x']
            self.y = self.player_info['y']
        else:
            self.x = -1
            self.y = -1

