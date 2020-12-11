from GamePlay import GamePlay
from BotGoTo import BotGoTo
from Client import get

gameId = 1
playerOne = 1
playerTwo = 2

get("http://localhost:9080/admin/createGame?gameId=" + str(gameId) +
    "&playerOne=" + str(playerOne) +
    "&playerTwo=" + str(playerTwo) +
    "&mapName=trialMap")

gamePlay = GamePlay('http://localhost:9080', gameId, playerOne, BotGoTo(24, 24))

gamePlay.play()
