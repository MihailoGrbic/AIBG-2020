from GamePlay import GamePlay
from BotBodyBlock import BotBodyBlock

gameId = 1
playerOne = 1
playerTwo = 2

gamePlay = GamePlay('http://localhost:9080', gameId, playerTwo, BotBodyBlock())

gamePlay.play()

