from GamePlaySingleBot import GamePlaySingleBot
from BotRandom import BotRandom
from BotRandomize import BotRandomize
from BotBuildSwordAndAttack import BotBuildSwordAndAttack
from BotBuildSwordAndAttackWithRunaway import BotBuildSwordAndAttackWithRunaway
from Client import get

gameId = 0
playerOne = 0
playerTwo = 1

get("http://localhost:9080/admin/createGame?gameId=" + str(gameId) +
           "&playerOne=" + str(playerOne) +
           "&playerTwo=" + str(playerTwo)  +
           "&mapName=mapConfig2")

gamePlay = GamePlaySingleBot('http://localhost:9080', gameId, playerOne, BotBuildSwordAndAttack(40))

gamePlay.play()

