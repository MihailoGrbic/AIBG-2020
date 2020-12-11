import Map
from utils import *
import actions

def get_all_non_digged(map: Map, currpos):
    tiles = []
    for x in range(map.width):
        for y in range(map.height):
            if 'tileType' in map.tiles[y][x] \
                    and map.tiles[y][x]['tileType'] == "DIGTILE" \
                    and map.tiles[y][x]["dug"] == False:
                tiles.append((x,y))

    tiles = sorted(tiles, key=lambda digtile: dist(currpos.x, currpos.y, digtile[0], digtile[1]))
    return tiles

def get_discovery_tiles_per_direction(map:Map, currpos):
    sol = {}
    sol[actions.up()] = calc_new_tiles(map, (currpos.x, currpos.y-1))
    sol[actions.down()] = calc_new_tiles(map, (currpos.x, currpos.y+1))
    sol[actions.left()] = calc_new_tiles(map, (currpos.x-1, currpos.y))
    sol[actions.right()] = calc_new_tiles(map, (currpos.x+1, currpos.y))
    return sol

def calc_new_tiles(map: Map, pos: (int,int)):
    if not within_bounds(map, pos):
        return -1
    new_tile_cnt = 0
    for xi in range(-3,3,1):
        for yi in range(-3,3,1):
            if abs(xi) + abs(yi) > 3:
                continue
            newx = pos[0] + xi
            newy = pos[1] + yi
            if within_bounds(map, (newx, newy)) and 'tileType' not in map.tiles[newy][newx]:
                new_tile_cnt += 1
    return new_tile_cnt

def within_bounds(map: Map, pos: (int,int)):
    return 0 <= pos[0] < map.width and 0 <= pos[1] < map.height