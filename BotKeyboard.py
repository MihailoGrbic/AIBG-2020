from Bot import Bot


class BotKeyboard(Bot):

    def play_single_turn(self, current_game_state):
        command = input("Your move, bitch: ")
        return command
