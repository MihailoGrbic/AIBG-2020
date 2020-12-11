from GameState import GameState
from Client import get


class GamePlay(object):
    def __init__(self, url, gameId, playerId, bot):
        self.url = url
        self.gameId = gameId

        self.playerId = playerId
        self.game_state: GameState = None

        self.bot = bot

        self.connect()


    def doAction(self, action):
        res = get('{0}/doAction?playerId={1}&gameId={2}&action={3}'.format(
            self.url, self.playerId, self.gameId, action))
        print('{0}/doAction?playerId={1}&gameId={2}&action={3}'.format(
            self.url, self.playerId, self.gameId, action))

        self.game_state.update_game_state(res)
        ss = self.game_state.self_info
        print("self player " + str(ss.x) + " " + str(ss.y))

    def play(self):
        while True:
            action = self.bot.play_single_turn(self.game_state)
            self.doAction(action)

    def connect(self):
        res = get(self.url + '/game/play?playerId=' + str(self.playerId) + '&gameId=' + str(self.gameId))
        self.game_state = GameState(res, self.gameId, self.playerId)
        print(res)