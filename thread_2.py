from GamePlay import GamePlay
from BotRotate import BotRotate as Bot
from EnemyBotCollectSell import EnemyBotCollectSell

gameId = 9
playerOne = 0
playerTwo = 1

gamePlay = GamePlay('http://localhost:9080', gameId, playerTwo, EnemyBotCollectSell())

gamePlay.play()

