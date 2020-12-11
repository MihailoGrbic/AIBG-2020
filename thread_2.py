from GamePlay import GamePlay
from BotRotate import BotRotate as Bot

gameId = 0
playerOne = 0
playerTwo = 1

gamePlay = GamePlay('http://localhost:9080', gameId, playerTwo, Bot())

gamePlay.play()

