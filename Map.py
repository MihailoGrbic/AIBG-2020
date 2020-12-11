class Map(object):
    def __init__(self, res):
        res = res['map']
        self.width = res['width']
        self.height = res['height']
        self.tiles = res['tiles']

        self.items = []
