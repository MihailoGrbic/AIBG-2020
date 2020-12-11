from GamePlay import GamePlay
from BotBodyBlock import BotBodyBlock

gameId = 0
playerOne = 0
playerTwo = 1

gamePlay = GamePlay('http://localhost:9080', gameId, playerTwo, BotBodyBlock())

gamePlay.play()

