from GameState import GameState
from Client import get

def default_state_of_mind():
    return {

    }


class GamePlay(object):
    def __init__(self, url, gameId, playerId, bot):
        self.url = url
        self.gameId = gameId

        self.playerId = playerId
        self.game_state: GameState = None

        self.bot = bot

        self.connect()

    def get_policy_list(self):
        return list()

    def get_child_bot(self):
        for policy in self.get_policy_list():
            if policy.should_execute(self.current_game_state):
                return policy.bot
        return None

    def doAction(self, a):
        res = get('{0}/doAction?playerId={1}&gameId={2}&action={3}'.format(
            self.url, self.playerId, self.gameId, a))
        print('{0}/doAction?playerId={1}&gameId={2}&action={3}'.format(
            self.url, self.playerId, self.gameId, a))

        self.current_game_state.update_game_state(res)
        ss = self.game_state.self_info
        print("self player " + str(ss.x) + " " + str(ss.y))

    def play(self):
        while True:
            action = self.bot.play_single_turn(self.game_state)
            self.doAction(action)

    def update_data(self, res):
        pass

    def connect(self):
        res = get(self.url + '/game/play?playerId=' + str(self.playerId) + '&gameId=' + str(self.gameId))
        self.game_state = GameState(res, self.gameId, self.playerId)
        print(res)