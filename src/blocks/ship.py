class Ship(object):
    def __init__(self, params):
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