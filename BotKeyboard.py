from Bot import Bot


class BotKeyboard(Bot):

    def __init__(self, dvorak: bool = False):
        self.dvorak = dvorak

    def play_single_turn(self, current_game_state):
        command = input("Your move, bitch: ")
        if self.dvorak:
            if command == ',':
                return 'w'
            if command == 'a':
                return 'a'
            if command == 'o':
                return 's'
            if command == 'e':
                return 'd'
        return command
