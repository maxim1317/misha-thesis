class Generator(object):
    def __init__(self, params):
        pass

    def next(self):
        from random import triangular
        from . import Ship

        ships = []
        ship_num = int(triangular(0, 3, 0))

        for i in range(ship_num):
            ships.append(Ship())

        return ships
