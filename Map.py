class Tile:

    def __init__(self, tile: dict):
        self.tile = tile
        self.x = tile.get('x', -1)
        self.y = tile.get('y', -1)
        self.blocked = tile.get('x', False)

    def __getitem__(self, item):
        return self.tile[item]

    def __setitem__(self, key, value):
        self.tile[key] = value
        if key == "x":
            self.x = value
        if key == "y":
            self.y = value


def create_tile_map(res_tiles):
    tiles = []
    for row in res_tiles:
        tiles.append([])
        for tile in row:
            tiles[-1].append(Tile(tile))
    return tiles


class Map(object):
    def __init__(self, res):
        res = res['map']
        self.size = 25
        self.width = res['width']
        self.height = res['height']
        self.tiles = create_tile_map(res['tiles'])

        self.tiles[11][11] = {'x':11, 'y':11, 'tileType':'BLOCKTILE', 'shop':True}
        self.tiles[12][11] = {'x':11, 'y':12, 'tileType':'BLOCKTILE', 'shop':True}
        self.tiles[13][11] = {'x':11, 'y':13, 'tileType':'BLOCKTILE', 'shop':True}
        self.tiles[11][12] = {'x':12, 'y':11, 'tileType':'BLOCKTILE', 'shop':True}
        self.tiles[12][12] = {'x':12, 'y':12, 'tileType':'BLOCKTILE', 'shop':True}
        self.tiles[13][12] = {'x':12, 'y':13, 'tileType':'BLOCKTILE', 'shop':True}
        self.tiles[11][13] = {'x':13, 'y':11, 'tileType':'BLOCKTILE', 'shop':True}
        self.tiles[12][13] = {'x':13, 'y':12, 'tileType':'BLOCKTILE', 'shop':True}
        self.tiles[13][13] = {'x':13, 'y':13, 'tileType':'BLOCKTILE', 'shop':True}

        self.items = []

    def reverse_corr(self, x, y):
        r_x = self.width - x - 1
        r_y = self.height - y - 1
        return r_x, r_y

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def update_tile(self, tile):
        for key in tile.keys():
            self.map[tile['y']][tile['x']][key] = tile[key]

    def mark_trap(self, x, y, trap_type):
        self.tiles[tile['y']][tile['x']]['is_trap'] = True
        self.tile[tile['y']][tile['x']]['trap_type'] = trap_type