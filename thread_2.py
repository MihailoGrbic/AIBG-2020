from GamePlay import GamePlay
from BotBodyBlock import BotBodyBlock
from  EnemyBotCollectSell import EnemyBotCollectSell

gameId = 12
playerOne = 0
playerTwo = 1

gamePlay = GamePlay('http://localhost:9080', gameId, playerTwo, EnemyBotCollectSell())

gamePlay.play()

