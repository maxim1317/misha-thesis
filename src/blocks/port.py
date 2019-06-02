class Unloading:
    def __init__(self, speed):
        self.speed = speed
        self.ship = None
        self.time_left = 0

    def load(self, ship):
        self.ship = ship
        self.time_left = int(ship.size / self.speed)  # хитрая формула

    def tick(self):
        if self.time_left > 0:
            self.time_left -= 1

    def ready(self):
        if self.time_left == 0:
            ship = self.ship
            self.ship = None
            return ship
        return None

    def free(self):
        if self.ship is None:
            return True
        return False


class Port(object):
    def __init__(self, params):
        self.unloadings = [Unloading(2)] * 3

    def free(self):
        free_u = []
        for u in range(len(self.unloadings)):
            if self.unloadings[u].free():
                free_u.append(u)
        return free_u

    def load(self, ship):
        for a in self.unloadings:
            if a.free():
                a.load(ship)
                return True
        return False

    def tick(self):
        for un in self.unloadings:
            un.tick()
