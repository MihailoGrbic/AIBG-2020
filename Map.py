class Map(object):
    def __init__(self, res):
        res = res['map']
        self.size = 25
        self.width = res['width']
        self.height = res['height']
        self.tiles = res['tiles']

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

    def update_tile(self, tile):
        for key in tile.keys():
            self.tiles[tile['y']][tile['x']][key] = tile[key]

    def mark_trap(self, x, y, trap_type):
        self.tiles[y][x]['is_trap'] = True
        self.tiles[y][x]['trap_type'] = trap_type