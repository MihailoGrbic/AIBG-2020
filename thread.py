from GamePlay import GamePlay
from EnemyBotCollectSell import EnemyBotCollectSell

SERVER_IP = "127.0.0.1"
MY_ID = 0
GAME_ID = 12

gamePlay = GamePlay('http://{}:9080'.format(SERVER_IP), GAME_ID, MY_ID, EnemyBotCollectSell())

gamePlay.play()