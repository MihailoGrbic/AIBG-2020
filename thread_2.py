from GamePlay import GamePlay
from BotRotate import BotRotate as Bot
from BotCollectSell import BotCollectSell

gameId = 7
playerOne = 0
playerTwo = 1

gamePlay = GamePlay('http://localhost:9080', gameId, playerTwo, BotCollectSell())

gamePlay.play()

