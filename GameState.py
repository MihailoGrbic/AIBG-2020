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
        self.state_of_mind = {}
        self.state_of_mind["TieTurns"] = 0
        self.state_of_mind["Peaceful"] = False
        self.state_of_mind["OpponentResources"] = 0
        self.state_of_mind["LastMoveWasStupid"] = False
        self.state_of_mind["AllSelfHealthDiff"] = 0

    def update_game_state(report):
        
        for tile in report['map']['tiles']:
            if bool(tile):
                
                x = tile['x']
                y = tile['y']
                pos = y*report['map']*width + x
                self.map['tiles'][pos] = tile