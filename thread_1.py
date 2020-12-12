from GamePlay import GamePlay
from BotJustBlockShop import BotJustBlockShop
from Client import get

gameId = 12
playerOne = 0
playerTwo = 1

get("http://localhost:9080/admin/createGame?gameId=" + str(gameId) +
    "&playerOne=" + str(playerOne) +
    "&playerTwo=" + str(playerTwo) +
    "&mapName=trialMap")

gamePlay = GamePlay('http://localhost:9080', gameId, playerOne, BotJustBlockShop())

gamePlay.play()
