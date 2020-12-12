from GamePlay import GamePlay
from BotBodyBlock import BotBodyBlock
from BotKeyboard import BotKeyboard

gameId = 1
playerOne = 1
playerTwo = 2

gamePlay = GamePlay('http://localhost:9080', gameId, playerTwo, BotKeyboard())

gamePlay.play()

