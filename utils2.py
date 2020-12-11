import Map
import utils

def dist(pos1: (int, int), pos2: (int, int)):
    return dist(pos1[0], pos1[1], pos2[0], pos2[1])

def get_all_non_digged(map: Map, currpos: (int, int)):
    tiles = []
    for x in range(map.width):
        for y in range(map.height):
            if map[x][y]['tileType'] == "DIGTILE" and map[x][y]["dug"] == False:
                tiles.append((x,y))

    tiles = sorted(tiles, key=lambda digtile: dist(currpos, digtile))
    return tiles

def get_discovery_tiles_per_direction(map:Map, currpos: (int,int)):
    sol = {}
    sol['w'] = calc_new_tiles(map, (currpos[0], currpos[1]-1))
    sol['s'] = calc_new_tiles(map, (currpos[0], currpos[1]+1))
    sol['a'] = calc_new_tiles(map, (currpos[0]-1, currpos[1]))
    sol['d'] = calc_new_tiles(map, (currpos[0]+1, currpos[1]))
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
            if within_bounds(map, (newx, newy)) and 'tileType' not in map[xi][yi]:
                new_tile_cnt += 1
    return new_tile_cnt

def within_bounds(map: Map, pos: (int,int)):
    return 0 <= pos[0] < map.width and 0 <= pos[1] < map.height