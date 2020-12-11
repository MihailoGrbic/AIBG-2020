from GamePlay import GamePlay
from BotGoTo import BotGoTo as Bot
from Client import get

gameId = 9
playerOne = 0
playerTwo = 1

get("http://localhost:9080/admin/createGame?gameId=" + str(gameId) +
    "&playerOne=" + str(playerOne) +
    "&playerTwo=" + str(playerTwo) +
    "&mapName=trialMap")

gamePlay = GamePlay('http://localhost:9080', gameId, playerOne, Bot(20, 20))

gamePlay.play()
