from GamePlay import GamePlay
from BotKeyboard import BotKeyboard

gameId = 0
playerOne = 0
playerTwo = 1

gamePlay = GamePlay('http://localhost:9080', gameId, playerTwo, BotKeyboard())

gamePlay.play()

