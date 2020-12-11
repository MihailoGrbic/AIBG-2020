from GamePlay import GamePlay
from BotGoTo import BotGoTo
from Client import get

gameId = 0
playerOne = 0
playerTwo = 1

get("http://localhost:9080/admin/createGame?gameId=" + str(gameId) +
    "&playerOne=" + str(playerOne) +
    "&playerTwo=" + str(playerTwo) +
    "&mapName=trialMap")

gamePlay = GamePlay('http://localhost:9080', gameId, playerOne, BotGoTo(10, 10))

gamePlay.play()
