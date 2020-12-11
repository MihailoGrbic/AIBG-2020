class Map(object):
    def __init__(self, res):
        res = res['map']
        self.width = res['width']
        self.height = res['height']
        self.tiles = res['tiles']

        self.items = []

    def reverse_corr(self, x, y):
        r_x = self.width - x - 1
        r_y = self.height - y - 1
        return r_x, r_y
