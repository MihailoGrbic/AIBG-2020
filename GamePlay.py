from GameState import GameState
from Client import get


class GamePlay(object):
    def __init__(self, url, gameId, playerId, bot):
        self.url = url
        self.gameId = gameId

        self.playerId = playerId
        self.current_game_state: GameState = None

        self.bot = bot

        self.connect()


    def doAction(self, action):
        res = get('{0}/doAction?playerId={1}&gameId={2}&action={3}'.format(
            self.url, self.playerId, self.gameId, action))
        print('{0}/doAction?playerId={1}&gameId={2}&action={3}'.format(
            self.url, self.playerId, self.gameId, action))

        self.current_game_state.update_game_state(res)

    def play(self):
        while True:
            action = self.bot.play_single_turn(self.current_game_state)
            self.doAction(action)

    def connect(self):
        res = get(self.url + '/game/play?playerId=' + str(self.playerId) + '&gameId=' + str(self.gameId))
        self.current_game_state.update_game_state(res)
        print(res)