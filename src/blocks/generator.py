class Ship(object):
    def __init__(self):
        import random

        self.cargo = {
            0: 1,
            1: 1,
            2: 2
        }
        self.size = random.randint(0, 10)

        # stats
        self.time_in_queue = 0
        self.time_in_movement = 0
        self.time_in_unloading = 0


class Generator(object):
    def __init__(self, params):
        pass

    def next(self):
        from random import triangular

        ships = []
        ship_num = int(triangular(0, 3, 0))

        for i in range(ship_num):
            ships.append(Ship())

        return ships
