import requests
import numpy as np
from time import sleep

SERVER_IP = "localhost"
MY_ID = "1"
GAME_ID = "2"

connect_player = "http://" + SERVER_IP + ":9080/game/play?playerId=" + MY_ID + "&gameId=" + GAME_ID
do_action = "http://" + SERVER_IP + ":9080/doAction?playerId=" + MY_ID + "&gameId=" + GAME_ID + "&action="

map_actions = [
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 'a', 'd', 
    
]

if __name__ == "__main__":
    connect_player = requests.get(connect_player)
    print(connect_player.content)

    for action in map_actions:
        resp = requests.get(do_action + action)
        print(resp.content)
        sleep(1)
